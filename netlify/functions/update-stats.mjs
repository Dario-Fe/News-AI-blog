import { getStore } from '@netlify/blobs';

export default async (req, context) => {
  console.log('Inizio aggregazione statistiche...');
  const store = getStore({ name: 'page-views' });
  let processedCount = 0;

  try {
    const { blobs } = await store.list();

    const allViews = [];

    const batchSize = 50;
    for (let i = 0; i < blobs.length; i += batchSize) {
      const batch = blobs.slice(i, i + batchSize);
      const results = await Promise.all(
        batch.map(async (entry) => {
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

    allViews.sort((a, b) => b.count - a.count);

    const summary = {
      lastUpdate: new Date().toISOString(),
      statsData: allViews,
      totalViews: allViews.reduce((sum, item) => sum + item.count, 0)
    };

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

export const config = {
  schedule: "@hourly"
};
