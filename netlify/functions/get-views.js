import { getStore } from '@netlify/blobs';

export default async () => {
  console.log("Function 'get-views' invoked.");

  try {
    const store = getStore('page-views');
    console.log("Blob store 'page-views' accessed.");

    const { blobs } = await store.list();
    console.log(`Found ${blobs.length} blob entries.`);

    if (blobs.length === 0) {
      console.log("No blobs found. Returning empty array.");
      return new Response(JSON.stringify([]), {
        status: 200,
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
      });
    }

    const allViews = await Promise.all(
      blobs.map(async (blob) => {
        try {
          const viewData = await store.get(blob.key, { type: 'json' });
          console.log(`Processing blob key: ${blob.key}, Data:`, viewData);
          return {
            path: blob.key,
            count: (viewData && viewData.count) ? viewData.count : 0,
          };
        } catch (e) {
          console.error(`Error processing individual blob key: ${blob.key}`, e);
          return { path: blob.key, count: 'Error' };
        }
      })
    );

    console.log("Successfully processed all blobs. Sorting data...");
    allViews.sort((a, b) => {
        if (typeof a.count !== 'number') return 1;
        if (typeof b.count !== 'number') return -1;
        return b.count - a.count;
    });

    console.log("Data sorted. Returning success response.");
    return new Response(JSON.stringify(allViews), {
      status: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });

  } catch (error) {
    console.error('CRITICAL ERROR in get-views function:', error);
    // Return a more detailed error message for debugging
    return new Response(JSON.stringify({ error: 'Internal Server Error', message: error.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' }
    });
  }
};