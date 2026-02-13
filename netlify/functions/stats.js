const ROWS_PER_PAGE = 20;

// Funzione per generare la pagina HTML iniziale
function generateHTML(initialData, totalRows, totalViews) {
  const tableRows = initialData.map(item => {
    const displayPath = `/${item.path}`;
    return `<tr><td>${displayPath}</td><td>${item.count}</td></tr>`;
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
            .total { font-weight: bold; margin-top: 20px; text-align: right; font-size: 1.1em; display: none; }
            #load-more-btn { display: block; width: 100%; padding: 10px; margin-top: 20px; background-color: #0056b3; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 1em; }
            #load-more-btn:hover { background-color: #004494; }
            #load-more-btn:disabled { background-color: #ccc; cursor: not-allowed; }
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
                <tbody id="stats-tbody">
                    ${tableRows}
                </tbody>
            </table>
            <button id="load-more-btn" ${totalRows <= ROWS_PER_PAGE ? 'style="display: none;"' : ''}>Carica Altre 20</button>
            <div class="total" id="total-views">Visite Totali: ${totalViews}</div>
        </div>
        <script>
            let currentPage = 1;
            let allStats = null;
            const totalRows = ${totalRows};
            const rowsPerPage = ${ROWS_PER_PAGE};

            const loadMoreBtn = document.getElementById('load-more-btn');
            const statsTbody = document.getElementById('stats-tbody');
            const totalViewsDiv = document.getElementById('total-views');

            async function fetchStats() {
                if (allStats) {
                    return allStats;
                }
                try {
                    const response = await fetch('/stats?format=json');
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    allStats = await response.json();
                    return allStats;
                } catch (error) {
                    console.error('Failed to fetch stats:', error);
                    loadMoreBtn.textContent = 'Errore nel caricamento';
                    throw error;
                }
            }

            function renderNextPage() {
                currentPage++;
                const start = (currentPage - 1) * rowsPerPage;
                const end = currentPage * rowsPerPage;
                const nextRows = allStats.slice(start, end);

                nextRows.forEach(item => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = \`<td>/\${item.path}</td><td>\${item.count}</td>\`;
                    statsTbody.appendChild(tr);
                });

                if (end >= totalRows) {
                    loadMoreBtn.style.display = 'none';
                    totalViewsDiv.style.display = 'block';
                }
            }

            loadMoreBtn.addEventListener('click', async () => {
                loadMoreBtn.disabled = true;
                loadMoreBtn.textContent = 'Caricamento...';

                try {
                    await fetchStats();
                    renderNextPage();
                } finally {
                    if (loadMoreBtn.style.display !== 'none') {
                        loadMoreBtn.disabled = false;
                        loadMoreBtn.textContent = 'Carica Altre 20';
                    }
                }
            });
        </script>
    </body>
    </html>
  `;
}

export default async (req, context) => {
  const { getStore } = await import('@netlify/blobs');
  
  const authHeader = req.headers.get('authorization');
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

    const url = new URL(req.url);
    const format = url.searchParams.get('format');

    if (format === 'json') {
      return new Response(JSON.stringify(allViews), {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const totalViewsCount = allViews.reduce((sum, item) => sum + item.count, 0);
    const initialData = allViews.slice(0, ROWS_PER_PAGE);
    
    const html = generateHTML(initialData, allViews.length, totalViewsCount);
    
    return new Response(html, {
      status: 200,
      headers: { 'Content-Type': 'text/html' },
    });

  } catch (error) {
    console.error('Error generating stats page:', error);
    return new Response('Error generating stats page.', { status: 500 });
  }
};
