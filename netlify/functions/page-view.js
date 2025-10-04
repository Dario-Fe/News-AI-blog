import { getStore } from '@netlify/blobs';

export default async (req) => {
  // 1. Assicurati che sia una richiesta POST
  if (req.method !== 'POST') {
    return new Response('Method Not Allowed', { status: 405 });
  }

  try {
    const { path } = await req.json();

    // 2. Valida il percorso per sicurezza
    if (!path || typeof path !== 'string' || !path.startsWith('/')) {
      return new Response('Invalid path', { status: 400 });
    }

    // Pulisce il percorso per evitare duplicati (es. con o senza / finale)
    const cleanedPath = path.endsWith('/') && path.length > 1 ? path.slice(0, -1) : path;
    
    const store = getStore('page-views');
    let currentViews = await store.get(cleanedPath, { type: 'json' }) || { count: 0 };
    
    // 3. Incrementa il contatore
    currentViews.count += 1;

    // 4. Salva il nuovo conteggio
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