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
//
// STORIA (settembre 2026): i confronti path-per-path fra gli snapshot notturni
// hanno dimostrato che il contatore dopo la patch è rigorosamente monotono
// (zero cali, zero path spariti), eppure il totale mostrato da /stats durante
// le raffiche di traffico salpava di ~150-250 unità rispetto a quanto lo
// snapshot successivo confermava. Un totale soprastimato non può nascere da
// letture in ritardo (eventual), che possono solo sottostimare: l'unico
// vettore plausibile è il LISTING PAGINATO, che sotto centinaia di scritture
// concorrenti può restituire la stessa chiave più di una volta mentre le
// pagine si spostano. Da qui i due interventi di questa versione:
//
//   1. DEDUPLICAZIONE delle chiavi dopo il listing + log del confronto
//      "chiavi elencate vs chiavi distinte": la prima ora in cui le due cifre
//      divergono, il colpevole del gonfiamento è fotografato nei log;
//   2. TRAIL ORARIO dei totali (__trail__): ogni giro lascia una riga con
//      totale, path e qualità, così le discrepanze restano attribuibili ora
//      per ora invece di evaporare col riepilogo sovrascritto.

const STORE_NAME = 'page-views';
const SUMMARY_KEY = '__summary__';
const TRAIL_KEY = '__trail__';
const LOST_PREFIX = '__lost__/';
const BATCH_SIZE = 50;
const ANOMALY_LIMIT = 25;      // quanti path elencare nel dettaglio
const LOST_DAYS_KEPT = 10;     // per quanti giorni tenere il conteggio delle scritture perse
const REGRESSION_MIN_LOST = 5; // sotto questa soglia il calo e' rumore, non un reset
const TRAIL_DAYS_KEPT = 30;    // retention del trail orario, in giorni
const TRAIL_SAME_HOUR_TOLERANCE_MS = 5 * 60 * 1000; // ritento entro l'ora: niente seconda riga

// NOTA sulle prestazioni (causa del timeout del 28/09/2026):
// i ~1600 contatori si leggono con la consistenza di default (eventual, servita
// dal edge) perche' il confronto avviene con un riepilogo vecchio di un'ora:
// una lettura in ritardo di 60 secondi non falsa nulla. La consistenza "strong"
// (che va sempre all'origin) resta solo sulla lettura del riepilogo precedente,
// dove serve il valore esatto. Con strong su tutte le letture la function superava
// il timeout, non riscriveva il riepilogo e la pagina /stats restava ferma.

function todayUtc() {
  return new Date().toISOString().slice(0, 10);
}

// Inquadra un timestamp nel suo bucket orario UTC ('2026-09-30T09:00:00.000Z').
// Il listing con pagina corrotta salta ore intere: senza normalizzazione le
// 10:00:53 e le 10:15:41 finirebbero in due bucket diversi.
function hourBucketUtc(iso) {
  const t = new Date(iso);
  if (Number.isNaN(t.getTime())) return null;
  return new Date(Math.floor(t.getTime() / 3600000) * 3600000).toISOString();
}

function jsonResponse(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export default async (req, context) => {
  console.log('Inizio aggregazione statistiche...');
  const store = getStore({ name: STORE_NAME });
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

    // Trail orario precedente: base su cui aggiungere la riga di questo giro.
    // La lettura NON è strong: un'ora di ritardo sul trail non falsa nulla.
    const previousTrail = await store.get(TRAIL_KEY, { type: 'json' });

    // 2. Elenco completo delle chiavi, con DEDUPLICAZIONE.
    //
    //    list({ paginate: true }) pagina automaticamente (1000 chiavi per
    //    pagina), ma mentre le pagine vengono scritte i blob si spostano da una
    //    pagina all'altra: la stessa chiave può comparire due volte (il totale
    //    soprastimato delle raffiche) o un'ora può essere saltata (una futura
    //    candela negativa). La deduplicazione con un Set elimina il primo
    //    problema e rende il secondo misurabile dai log.
    const keys = [];        // chiavi DISTINTE da leggere
    const seen = new Set();
    let listedKeys = 0;     // quante chiavi ha prodotto il listing, prima della dedup
    let duplicateKeys = 0;  // chiavi viste più di una volta
    const lostByDay = {};
    for await (const page of store.list({ paginate: true })) {
      for (const entry of page.blobs) {
        const key = entry.key;
        if (key === SUMMARY_KEY || key === TRAIL_KEY) continue;

        if (key.startsWith(LOST_PREFIX)) {
          const day = key.slice(LOST_PREFIX.length, LOST_PREFIX.length + 10);
          if (/^\d{4}-\d{2}-\d{2}$/.test(day)) {
            lostByDay[day] = (lostByDay[day] || 0) + 1;
          }
          continue;
        }

        listedKeys += 1;
        if (seen.has(key)) {
          duplicateKeys += 1;
          continue;
        }
        seen.add(key);
        keys.push(key);
      }
    }

    if (duplicateKeys > 0) {
      console.warn(
        `Listing paginato: ${listedKeys} chiavi elencate ma solo ${keys.length} distinte ` +
        `(${duplicateKeys} duplicate). Il totale del riepilogo PRECEDENTE potrebbe essere gonfiato.`
      );
    } else {
      console.log(`Listing paginato: ${listedKeys} chiavi, tutte distinte.`);
    }

    // 3. Lettura dei contatori a batch.
    const allViews = [];
    const unreadable = [];
    for (let i = 0; i < keys.length; i += BATCH_SIZE) {
      const batch = keys.slice(i, i + BATCH_SIZE);
      const results = await Promise.all(
        batch.map(async (key) => {
          try {
            const data = await store.get(key, { type: 'json' });
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
    let ignoredDips = 0;
    let ignoredDipsViews = 0;
    for (const item of allViews) {
      const prev = previousCounts.get(item.path);
      if (prev === undefined || item.unreadable) continue;
      if (item.count < prev) {
        const lost = prev - item.count;
        // Cali piccoli possono essere il ritardo di propagazione di una lettura
        // eventual: si contano a parte, non come reset.
        if (lost < REGRESSION_MIN_LOST) {
          ignoredDips += 1;
          ignoredDipsViews += lost;
          continue;
        }
        regressedViews += lost;
        if (regressions.length < ANOMALY_LIMIT) {
          regressions.push({ path: item.path, from: prev, to: item.count, lost });
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

    // 5-bis. TRAIL ORARIO dei totali.
    //
    // Il riepilogo viene sovrascritto a ogni giro: se un totale anomalamente
    // alto (o un calo) passa per un'ora, alle ore successive non resta traccia
    // e la discrepanza con lo snapshot notturno diventa non attribuibile. Ogni
    // giro appende qui una riga (bucket orario UTC) con totale, path e qualità.
    const nowIso = new Date().toISOString();
    const thisHour = hourBucketUtc(nowIso);
    const droppedWritesToday = droppedWrites[todayUtc()] || 0;

    const trail = { updatedAt: nowIso, buckets: {} };
    if (previousTrail && previousTrail.buckets) {
      const minBucket = hourBucketUtc(
        new Date(Date.now() - TRAIL_DAYS_KEPT * 86400000).toISOString()
      );
      for (const [bucket, row] of Object.entries(previousTrail.buckets)) {
        if (minBucket && bucket < minBucket) continue;
        trail.buckets[bucket] = row;
      }
    }

    // "Run now" a pochi minuti di distanza: non ammucchiamo righe nella stessa ora.
    const lastSameHour = trail.buckets[thisHour];
    const shouldAppend = !lastSameHour ||
      Date.now() - Date.parse(lastSameHour.at) >= TRAIL_SAME_HOUR_TOLERANCE_MS;

    if (shouldAppend) {
      trail.buckets[thisHour] = {
        at: nowIso,
        totalViews,
        paths: keys.length,
        listedKeys,
        duplicateKeys,
        regressions: regressions.length,
        regressedViews,
        missing: missing.length,
        missingViews,
        unreadable: unreadable.length,
        droppedWritesToday,
        ignoredDips,
      };
      try {
        await store.setJSON(TRAIL_KEY, trail);
        console.log(`Trail orario aggiornato: ${thisHour}, totale ${totalViews}.`);
      } catch (error) {
        // Il trail è diagnostica, non dato: un fallimento non deve fermare il riepilogo.
        console.error('Impossibile aggiornare il trail orario:', error);
      }
    }

    const summary = {
      lastUpdate: new Date().toISOString(),
      statsData: allViews.map((item) => ({ path: item.path, count: item.count })),
      totalViews,
      paths: allViews.length,
      dataQuality: {
        previousTotal,
        totalChange: previousTotal === null ? null : totalViews - previousTotal,
        // Diagnostica listing: chiavi elencate vs distinte. duplicateKeys > 0
        // implica che il totalViews di QUESTO riepilogo può essere gonfiato
        // (una chiave duplicata conta due volte) e che i log vanno guardati.
        dedupe: { listedKeys, distinctKeys: keys.length, duplicateKeys },
        regressions,
        regressionsCount: regressions.length,
        regressedViews,
        ignoredDips,
        ignoredDipsViews,
        missing,
        missingCount: missing.length,
        missingViews,
        unreadable,
        unreadableCount: unreadable.length,
        droppedWritesToday,
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
      totalViews,
      lastUpdate: summary.lastUpdate,
      listedKeys,
      distinctKeys: keys.length,
      duplicateKeys,
      dedupe: summary.dataQuality.dedupe,
      regressions: summary.dataQuality.regressionsCount,
      droppedWritesToday,
      trail: shouldAppend ? 'scritto' : 'invariato (riga già presente per questa ora)',
    });
  } catch (error) {
    console.error(`Errore critico durante l'aggregazione:`, error);
    return new Response(`Errore aggregazione: ${error.message}`, { status: 500 });
  }
};

export const config = {
  schedule: "@hourly"
};
