import { getStore } from '@netlify/blobs';

/**
 * Questa funzione aggrega periodicamente i dati delle visualizzazioni
 * per evitare il timeout della pagina delle statistiche.
 * Viene eseguita automaticamente ogni ora.
 */
export default async (req, context) => {
  console.log('Inizio aggregazione statistiche...');
  const store = getStore({ name: 'page-views' });
  const allViews = [];
  let cursor = null;
  let processedCount = 0;

  try {
    // 1. Ciclo attraverso tutti i blob esistenti (gestendo la paginazione)
    do {
      const listResult = await store.list({ cursor, limit: 1000 });
      // Gestione difensiva per diverse versioni dell'SDK (blobs vs entries)
      const entries = listResult.blobs || listResult.entries || [];

      // Elaborazione a blocchi per massimizzare l'efficienza
      const batchSize = 50;
      for (let i = 0; i < entries.length; i += batchSize) {
        const batch = entries.slice(i, i + batchSize);
        const results = await Promise.all(
          batch.map(async (entry) => {
            // Saltiamo il file di riepilogo stesso
            if (entry.key === '__summary__') return null;

            try {
              const data = await store.get(entry.key, { type: 'json' });
              return {
                path: entry.key,
                count: (data && typeof data.count === 'number') ? data.count : 0
              };
            } catch (e) {
              console.error(`Errore nel recupero del blob ${entry.key}:`, e);
              return null;
            }
          })
        );

        allViews.push(...results.filter(item => item !== null));
        processedCount += batch.length;
        console.log(`Processati ${processedCount} record...`);
      }

      cursor = listResult.next_cursor || listResult.cursor;
    } while (cursor);

    // 2. Ordinamento per visualizzazioni decrescenti
    allViews.sort((a, b) => b.count - a.count);

    // 3. Creazione dell'oggetto di riepilogo
    const summary = {
      lastUpdate: new Date().toISOString(),
      statsData: allViews,
      totalViews: allViews.reduce((sum, item) => sum + item.count, 0)
    };

    // 4. Salvataggio del riepilogo in un unico blob dedicato
    await store.setJSON('__summary__', summary);

    console.log('Aggregazione completata con successo.');

    return new Response(JSON.stringify({
      success: true,
      processed: processedCount,
      lastUpdate: summary.lastUpdate
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });

  } catch (error) {
    console.error('Errore critico durante l\'aggregazione:', error);
    return new Response(`Errore aggregazione: ${error.message}`, { status: 500 });
  }
};

// Configurazione per l'esecuzione pianificata (Netlify Scheduled Functions)
export const config = {
  schedule: "@hourly"
};
