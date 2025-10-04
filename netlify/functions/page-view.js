export default async (req) => {
  // Use dynamic import to resolve the ESM/CJS conflict
  const { getStore } = await import('@netlify/blobs');

  // --- DIAGNOSTIC ---
  console.log(`page-view function invoked. Method: ${req.method}`);

  if (req.method !== 'POST') {
    return new Response('Method Not Allowed', { status: 405 });
  }

  try {
    // --- DIAGNOSTIC: Log the raw body ---
    const rawBody = await req.text();
    console.log("Raw request body received:", rawBody);

    // Now, attempt to parse it
    const data = JSON.parse(rawBody);
    const path = data.path;

    if (!path || typeof path !== 'string' || !path.startsWith('/')) {
      console.error("Invalid path received:", path);
      return new Response('Invalid path', { status: 400 });
    }

    const cleanedPath = path.endsWith('/') && path.length > 1 ? path.slice(0, -1) : path;
    
    const store = getStore('page-views');
    let currentViews = await store.get(cleanedPath, { type: 'json' }) || { count: 0 };
    
    currentViews.count += 1;

    await store.setJSON(cleanedPath, currentViews);
    
    console.log(`Successfully updated view count for ${cleanedPath} to ${currentViews.count}`);

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });

  } catch (error) {
    console.error('CRITICAL ERROR in page-view function:', error);
    return new Response('Internal Server Error', { status: 500 });
  }
};