// Helper function to generate the HTML page
function generateHTML(statsData) {
  let totalViews = 0;
  statsData.forEach(item => totalViews += item.count);

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
            
            #view-more-container {
                display: flex;
                justify-content: center;
                margin-top: 20px;
                margin-bottom: 20px;
            }
            .view-more-button {
                background-color: #ffffff;
                padding: 10px 20px;
                border-radius: 6px;
                text-decoration: none;
                color: #1c1e21;
                font-weight: bold;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transition: all 0.2s;
                border: 1px solid #dddfe2;
                cursor: pointer;
            }
            .view-more-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
                background-color: #f8f9fa;
            }
            .view-more-button:disabled {
                background-color: #e9ebee;
                color: #bec3c9;
                cursor: not-allowed;
                transform: none;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
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
                <tbody id="stats-body">
                    <!-- Rows will be injected here by JavaScript -->
                </tbody>
            </table>
            
            <div id="view-more-container">
                <button id="view-more-button" class="view-more-button">Visualizza altro</button>
            </div>

            <div class="total">Visite Totali: ${totalViews}</div>
        </div>

        <script>
            const statsData = ${JSON.stringify(statsData)};
            let currentPage = 0;
            const rowsPerPage = 20;
            
            const statsBody = document.getElementById('stats-body');
            const viewMoreButton = document.getElementById('view-more-button');
            const viewMoreContainer = document.getElementById('view-more-container');

            function renderNextRows() {
                const start = currentPage * rowsPerPage;
                const end = start + rowsPerPage;
                const rowsToRender = statsData.slice(start, end);

                rowsToRender.forEach(item => {
                    const row = document.createElement('tr');
                    const displayPath = '/' + item.path;
                    row.innerHTML = '<td>' + displayPath + '</td><td>' + item.count + '</td>';
                    statsBody.appendChild(row);
                });

                currentPage++;

                if (currentPage * rowsPerPage >= statsData.length) {
                    viewMoreContainer.style.display = 'none';
                }
            }

            viewMoreButton.addEventListener('click', renderNextRows);

            // Initial render
            renderNextRows();
        </script>
    </body>
    </html>
  `;
}


import { getStore } from '@netlify/blobs';

export default async (req, context) => {
  // 1. Authentication Check (Fastest check first)
  const authHeader = req.headers.get('authorization');
  const user = process.env.STATS_USER;
  const pass = process.env.STATS_PASSWORD;

  if (!user || !pass) {
    return new Response('Authentication not configured on server.', { status: 500 });
  }

  const expectedAuth = 'Basic ' + Buffer.from(`${user}:${pass}`).toString('base64');
  if (authHeader !== expectedAuth) {
    return new Response('Unauthorized', {
      status: 401,
      headers: { 'WWW-Authenticate': 'Basic realm="Restricted Area"' },
    });
  }

  // 2. Fetch and process data
  try {
    const store = getStore({ name: 'page-views' });
    
    // List blobs with a limit to avoid timeouts if the site has thousands of pages
    const { blobs } = await store.list({ limit: 1000 });
    
    // Process blobs in batches of 50 to avoid hitting concurrency limits or timing out
    const allViews = [];
    const batchSize = 50;
    
    for (let i = 0; i < blobs.length; i += batchSize) {
      const batch = blobs.slice(i, i + batchSize);
      const batchResults = await Promise.all(
        batch.map(async (blob) => {
          try {
            const viewData = await store.get(blob.key, { type: 'json' });
            return {
              path: blob.key,
              count: (viewData && typeof viewData.count === 'number') ? viewData.count : 0,
            };
          } catch (e) {
            console.error(`Error fetching blob ${blob.key}:`, e);
            return null; // Skip failed blobs
          }
        })
      );
      allViews.push(...batchResults.filter(item => item !== null));
    }

    // Sort by views descending
    allViews.sort((a, b) => b.count - a.count);
    
    // 3. Render the full HTML page with the data
    const html = generateHTML(allViews);
    
    return new Response(html, {
      status: 200,
      headers: { 
        'Content-Type': 'text/html',
        'Cache-Control': 'no-store, max-age=0' // Ensure fresh data on every visit
      },
    });

  } catch (error) {
    console.error('Critical error generating stats page:', error);
    return new Response(`Server error while processing statistics: ${error.message}`, { status: 500 });
  }
};
