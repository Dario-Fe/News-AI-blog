import { getStore } from '@netlify/blobs';

export default async () => {
  try {
    const store = getStore('page-views');
    const { blobs } = await store.list();

    const allViews = await Promise.all(
      blobs.map(async (blob) => {
        const viewData = await store.get(blob.key, { type: 'json' });
        return {
          path: blob.key,
          count: viewData.count || 0,
        };
      })
    );

    // Ordina i risultati per numero di visite, dal più alto al più basso
    allViews.sort((a, b) => b.count - a.count);

    return new Response(JSON.stringify(allViews), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*', // Permette al frontend di chiamare questa funzione
      },
    });

  } catch (error) {
    console.error('Error fetching page views:', error);
    return new Response('Internal Server Error', { status: 500 });
  }
};