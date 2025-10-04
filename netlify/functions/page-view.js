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

    const cleanedPath = path.endsWith('/') && path.length > 1 ? path.slice(0, -1) : path;
    
    const store = getStore('page-views');
    let currentViews = await store.get(cleanedPath, { type: 'json' }) || { count: 0 };
    
    currentViews.count += 1;

    await store.setJSON(cleanedPath, currentViews);

    return new Response(JSON.stringify({ success: true, path: cleanedPath, count: currentViews.count }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });

  } catch (error) {
    console.error('Error processing page view:', error);
    return new Response('Internal Server Error', { status: 500 });
  }
};