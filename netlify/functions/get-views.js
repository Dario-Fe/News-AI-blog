import { getStore } from '@netlify/blobs';

export default async () => {
  try {
    const store = getStore('page-views');
    const blobs = await store.list(); // The result is the array directly

    const allViews = await Promise.all(
      blobs.map(async (blob) => {
        const viewData = await store.get(blob.key, { type: 'json' });
        return {
          path: blob.key,
          count: (viewData && viewData.count) ? viewData.count : 0,
        };
      })
    );

    // Sort the results by view count, descending
    allViews.sort((a, b) => b.count - a.count);

    return new Response(JSON.stringify(allViews), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });

  } catch (error) {
    console.error('CRITICAL ERROR in get-views function:', error);
    return new Response(JSON.stringify({ error: 'Internal Server Error', message: error.message }), { 
        status: 500,
        headers: { 'Content-Type': 'application/json' }
    });
  }
};