export default async (req) => {
  // Use dynamic import to resolve the ESM/CJS conflict
  const { getStore } = await import('@netlify/blobs');

  if (req.method !== 'POST') {
    return new Response('Method Not Allowed', { status: 405 });
  }

  try {
    const { path } = await req.json();

    if (!path || typeof path !== 'string' || !path.startsWith('/')) {
      return new Response('Invalid path', { status: 400 });
    }

    // The key for the blob store cannot start with a slash.
    const storeKey = path.startsWith('/') ? path.slice(1) : path;

    const store = getStore('page-views');
    let currentViews = await store.get(storeKey, { type: 'json' }) || { count: 0 };
    
    currentViews.count += 1;

    await store.setJSON(storeKey, currentViews);

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });

  } catch (error) {
    console.error('Error in page-view function:', error);
    return new Response('Internal Server Error', { status: 500 });
  }
};