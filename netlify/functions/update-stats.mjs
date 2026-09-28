import { getStore } from '@netlify/blobs';

// Riepilogo orario dei contatori visite.
//
// Oltre al riepilogo (statsData / totalViews) che alimenta la pagina /stats e
// generate_daily_stats.py, questa funzione confronta i contatori con il riepilogo
// precedente e REGISTRA GLI SCALI invece di nasconderli:
//
//   dataQuality.regressions   -> path il cui contatore è tornato indietro
//                                (con le visite perse)
//   dataQuality.missing       -> path presenti prima e spariti adesso
//   dataQuality.unreadable    -> blob illeggibili o con count non numerico
//                                (si conserva l'ultimo valore noto, non si azzera)
//   dataQuality.droppedWrites -> visite che page-view.mjs non è riuscito a
//                                incrementare (blob __lost__/YYYY-MM-DD/...)
//
// Queste informazioni viaggiano dentro __summary__ e quindi finiscono nel JSON
// servito da stats.mjs (?format=json), che è la sorgente del brief giornaliero.

const STORE_NAME = 'page-views';
const SUMMARY_KEY = '__summary__';
const LOST_PREFIX = '__lost__/';
const BATCH_SIZE = 50;
const ANOMALY_LIMIT = 25;   // quanti path elencare nel dettaglio
const LOST_DAYS_KEPT = 10;  // per quanti giorni tenere il conteggio delle scritture perse

function todayUtc() {
  return new Date().toISOString().slice(0, 10);
}

function jsonResponse(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export default async (req, context) => {
  console.log('Inizio aggregazione statistiche...');
  const store = getStore({ name: STORE_NAME, consistency: 'strong' });
  let processedCount = 0;

  try {
    // 1. Riepilogo precedente: serve per confrontare i contatori e per non
    //    azzerare un path che al momento non riusciamo a leggere.
    const previous = await store.get(SUMMARY_KEY, { type: 'json', consistency: 'strong' });
    const previousCounts = new Map();
    if (previous && Array.isArray(previous.statsData)) {
      for (const item of previous.statsData) {
        previousCounts.set(item.path, item.count);
      }
    }

    // 2. Elenco completo delle chiavi. list() pagina automaticamente (1000 voci
    //    per pagina), quindi va usato { paginate: true } per non perdere i path
    //    oltre la prima pagina.
    const keys = [];
    const lostByDay = {};
    for await (const page of store.list({ paginate: true })) {
      for (const entry of page.blobs) {
        if (entry.key === SUMMARY_KEY) continue;

        if (entry.key.startsWith(LOST_PREFIX)) {
          const day = entry.key.slice(LOST_PREFIX.length, LOST_PREFIX.length + 10);
          if (/^\d{4}-\d{2}-\d{2}$/.test(day)) {
            lostByDay[day] = (lostByDay[day] || 0) + 1;
          }
          continue;
        }

        keys.push(entry.key);
      }
    }

    // 3. Lettura dei contatori a batch.
    const allViews = [];
    const unreadable = [];
    for (let i = 0; i < keys.length; i += BATCH_SIZE) {
      const batch = keys.slice(i, i + BATCH_SIZE);
      const results = await Promise.all(
        batch.map(async (key) => {
          try {
            const data = await store.get(key, { type: 'json', consistency: 'strong' });
            if (!data || typeof data.count !== 'number' || !Number.isFinite(data.count)) {
              return { path: key, count: null, reason: data ? 'count non numerico' : 'blob vuoto' };
            }
            return { path: key, count: data.count };
          } catch (error) {
            console.error(`Errore nel recupero del blob ${key}:`, error);
            return { path: key, count: null, reason: 'errore di lettura' };
          }
        })
      );

      for (const item of results) {
        if (item.count === null) {
          const fallback = previousCounts.get(item.path) ?? 0;
          unreadable.push({ path: item.path, reason: item.reason, fallback });
          allViews.push({ path: item.path, count: fallback, unreadable: true });
        } else {
          allViews.push({ path: item.path, count: item.count });
        }
      }

      processedCount += batch.length;
      console.log(`Processati ${processedCount} record...`);
    }

    allViews.sort((a, b) => b.count - a.count);

    // 4. Confronto con il riepilogo precedente: cali, path spariti.
    const present = new Set(allViews.map((item) => item.path));

    const regressions = [];
    let regressedViews = 0;
    for (const item of allViews) {
      const prev = previousCounts.get(item.path);
      if (prev === undefined || item.unreadable) continue;
      if (item.count < prev) {
        regressedViews += prev - item.count;
        if (regressions.length < ANOMALY_LIMIT) {
          regressions.push({ path: item.path, from: prev, to: item.count, lost: prev - item.count });
        }
      }
    }

    const missing = [];
    let missingViews = 0;
    for (const [path, count] of previousCounts) {
      if (present.has(path)) continue;
      missingViews += count;
      if (missing.length < ANOMALY_LIMIT) {
        missing.push({ path, count });
      }
    }

    // 5. Scritture perse annotate da page-view.mjs, ultimi LOST_DAYS_KEPT giorni.
    const cutoff = new Date(Date.now() - LOST_DAYS_KEPT * 86400000).toISOString().slice(0, 10);
    const droppedWrites = {};
    for (const [day, count] of Object.entries(lostByDay)) {
      if (day >= cutoff) droppedWrites[day] = count;
    }

    const totalViews = allViews.reduce((sum, item) => sum + item.count, 0);
    const previousTotal = previous && typeof previous.totalViews === 'number' ? previous.totalViews : null;

    const summary = {
      lastUpdate: new Date().toISOString(),
      statsData: allViews.map((item) => ({ path: item.path, count: item.count })),
      totalViews,
      paths: allViews.length,
      dataQuality: {
        previousTotal,
        totalChange: previousTotal === null ? null : totalViews - previousTotal,
        regressions,
        regressionsCount: regressions.length,
        regressedViews,
        missing,
        missingCount: missing.length,
        missingViews,
        unreadable,
        unreadableCount: unreadable.length,
        droppedWritesToday: droppedWrites[todayUtc()] || 0,
        droppedWrites,
      },
    };

    if (regressedViews > 0) {
      console.warn(`Contatori tornati indietro: ${regressions.length} path, ${regressedViews} visite perse.`);
    }
    if (missingViews > 0) {
      console.warn(`Path spariti dal contatore: ${missing.length} path, ${missingViews} visite.`);
    }
    if (unreadable.length > 0) {
      console.warn(`Blob illeggibili: ${unreadable.length} (conservato l'ultimo valore noto).`);
    }

    await store.setJSON(SUMMARY_KEY, summary);

    console.log('Aggregazione completata con successo.');

    return jsonResponse({
      success: true,
      processed: processedCount,
      paths: allViews.length,
      lastUpdate: summary.lastUpdate,
      regressions: summary.dataQuality.regressionsCount,
      droppedWritesToday: summary.dataQuality.droppedWritesToday,
    });
  } catch (error) {
    console.error('Errore critico durante l\'aggregazione:', error);
    return new Response(`Errore aggregazione: ${error.message}`, { status: 500 });
  }
};

export const config = {
  schedule: "@hourly"
};
