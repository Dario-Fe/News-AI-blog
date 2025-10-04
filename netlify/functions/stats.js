// Helper function to generate the HTML page
function generateHTML(statsData) {
  let totalViews = 0;
  const tableRows = statsData.map(item => {
    totalViews += item.count;
    return `<tr><td>${item.path}</td><td>${item.count}</td></tr>`;
  }).join('');

  return `
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Statistiche Visite - AITalk</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; margin: 0; background-color: #f0f2f5; color: #1c1e21; padding: 20px; }
            h1 { text-align: center; color: #0056b3; }
            #stats-container { max-width: 900px; margin: 20px auto; background-color: #fff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); padding: 20px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background-color: #f8f9fa; font-weight: bold; }
            tr:hover { background-color: #f0f2f5; }
            .total { font-weight: bold; margin-top: 20px; text-align: right; font-size: 1.1em; }
        </style>
    </head>
    <body>
        <div id="stats-container">
            <h1>Statistiche Visite Anonime</h1>
            <table>
                <thead>
                    <tr>
                        <th>Pagina</th>
                        <th>Visite</th>
                    </tr>
                </thead>
                <tbody>
                    ${tableRows}
                </tbody>
            </table>
            <div class="total">Visite Totali: ${totalViews}</div>
        </div>
    </body>
    </html>
  `;
}


export default async (req, context) => {
  // Use dynamic import to resolve the ESM/CJS conflict
  const { getStore } = await import('@netlify/blobs');
  
  // 1. Authentication
  const authHeader = req.headers.get('authorization');
  // Use process.env for Node.js runtime on Netlify
  const user = process.env.STATS_USER;
  const pass = process.env.STATS_PASSWORD;

  if (!user || !pass) {
    return new Response('Authentication not configured.', { status: 500 });
  }

  const expectedAuth = 'Basic ' + btoa(`${user}:${pass}`);
  if (authHeader !== expectedAuth) {
    return new Response('Unauthorized', {
      status: 401,
      headers: { 'WWW-Authenticate': 'Basic realm="Restricted Area"' },
    });
  }

  // 2. If authenticated, fetch data
  try {
    const store = getStore('page-views');
    const { blobs } = await store.list();
    
    const allViews = await Promise.all(
      blobs.map(async (blob) => {
        const viewData = await store.get(blob.key, { type: 'json' });
        return {
          path: blob.key,
          count: (viewData && viewData.count) ? viewData.count : 0,
        };
      })
    );

    allViews.sort((a, b) => b.count - a.count);
    
    // 3. Render the full HTML page with the data
    const html = generateHTML(allViews);
    
    return new Response(html, {
      status: 200,
      headers: { 'Content-Type': 'text/html' },
    });

  } catch (error) {
    console.error('Error generating stats page:', error);
    return new Response('Error generating stats page.', { status: 500 });
  }
};