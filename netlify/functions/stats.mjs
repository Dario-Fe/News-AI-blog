// Funzione per generare la pagina HTML delle statistiche
function generateHTML(statsData, lastUpdate) {
  let totalViews = 0;
  statsData.forEach(item => totalViews += item.count);

  const formattedDate = lastUpdate ? new Date(lastUpdate).toLocaleString('it-IT') : 'In fase di aggiornamento...';

  return `
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Statistiche Visite - AITalk</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; margin: 0; background-color: #f0f2f5; color: #1c1e21; padding: 20px; }
            h1 { text-align: center; color: #0056b3; margin-bottom: 5px; }
            .last-update { text-align: center; color: #65676b; font-size: 0.9em; margin-bottom: 20px; }
            #stats-container { max-width: 900px; margin: 20px auto; background-color: #fff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); padding: 20px; }
            
            /* Stili della Barra di Ricerca */
            .search-wrapper {
                position: relative;
                margin-top: 20px;
                margin-bottom: 15px;
            }
            .search-input {
                width: 100%;
                padding: 12px 40px 12px 16px;
                font-size: 1em;
                border: 1px solid #dddfe2;
                border-radius: 8px;
                box-sizing: border-box;
                outline: none;
                transition: border-color 0.2s, box-shadow 0.2s;
            }
            .search-input:focus {
                border-color: #0056b3;
                box-shadow: 0 0 0 2px rgba(0, 86, 179, 0.1);
            }
            .search-clear {
                position: absolute;
                right: 12px;
                top: 50%;
                transform: translateY(-50%);
                background: none;
                border: none;
                font-size: 1.2em;
                color: #8a8d91;
                cursor: pointer;
                display: none;
                padding: 4px;
                line-height: 1;
            }
            .search-clear:hover {
                color: #1c1e21;
            }

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
        </style>
    </head>
    <body>
        <div id="stats-container">
            <h1>Statistiche Visite Anonime</h1>
            <div class="last-update">Ultimo aggiornamento: ${formattedDate}</div>
            
            <!-- Barra di Ricerca -->
            <div class="search-wrapper">
                <input type="text" id="search-input" class="search-input" placeholder="Cerca una pagina o articolo (es. /en/ o titolo)..." autocomplete="off">
                <button id="search-clear" class="search-clear" title="Cancella ricerca">&times;</button>
            </div>

            <table>
                <thead>
                    <tr>
                        <th>Pagina</th>
                        <th>Visite</th>
                    </tr>
                </thead>
                <tbody id="stats-body">
                    <!-- Righe caricate da JS -->
                </tbody>
            </table>
            
            <div id="view-more-container">
                <button id="view-more-button" class="view-more-button">Visualizza altro</button>
            </div>

            <div class="total" id="total-views">Visite Totali: ${totalViews}</div>
        </div>

        <script>
            const statsData = ${JSON.stringify(statsData)};
            let filteredData = [...statsData];
            let currentPage = 0;
            const rowsPerPage = 25;
            
            const statsBody = document.getElementById('stats-body');
            const viewMoreButton = document.getElementById('view-more-button');
            const viewMoreContainer = document.getElementById('view-more-container');
            const searchInput = document.getElementById('search-input');
            const searchClear = document.getElementById('search-clear');
            const totalElement = document.getElementById('total-views');

            const totalViews = ${totalViews};

            function renderNextRows() {
                const start = currentPage * rowsPerPage;
                const end = start + rowsPerPage;
                const rowsToRender = filteredData.slice(start, end);

                if (filteredData.length === 0 && currentPage === 0) {
                    statsBody.innerHTML = '<tr><td colspan="2" style="text-align: center; color: #65676b; padding: 20px;">Nessun risultato trovato</td></tr>';
                    viewMoreContainer.style.display = 'none';
                    return;
                }

                rowsToRender.forEach(item => {
                    const row = document.createElement('tr');
                    const displayPath = item.path.startsWith('/') ? item.path : '/' + item.path;
                    row.innerHTML = '<td>' + displayPath + '</td><td>' + item.count + '</td>';
                    statsBody.appendChild(row);
                });

                currentPage++;

                if (currentPage * rowsPerPage >= filteredData.length) {
                    viewMoreContainer.style.display = 'none';
                } else {
                    viewMoreContainer.style.display = 'flex';
                }
            }

            function updateSummary() {
                const query = searchInput.value.toLowerCase().trim();
                
                if (query) {
                    searchClear.style.display = 'block';
                    filteredData = statsData.filter(item => {
                        const displayPath = item.path.startsWith('/') ? item.path : '/' + item.path;
                        return displayPath.toLowerCase().includes(query);
                    });
                } else {
                    searchClear.style.display = 'none';
                    filteredData = [...statsData];
                }

                // Ricalcola il totale delle visite filtrate
                let filteredTotal = 0;
                filteredData.forEach(item => filteredTotal += item.count);

                if (query) {
                    totalElement.innerHTML = 'Visite Totali filtrate: ' + filteredTotal + ' <span style="font-weight: normal; font-size: 0.9em; color: #65676b;">(su un totale di ' + totalViews + ')</span>';
                } else {
                    totalElement.textContent = 'Visite Totali: ' + totalViews;
                }

                currentPage = 0;
                statsBody.innerHTML = '';
                renderNextRows();
            }

            searchInput.addEventListener('input', updateSummary);

            searchClear.addEventListener('click', () => {
                searchInput.value = '';
                updateSummary();
                searchInput.focus();
            });

            viewMoreButton.addEventListener('click', renderNextRows);

            // Caricamento iniziale
            updateSummary();
        </script>
    </body>
    </html>
  `;
}

import { getStore } from '@netlify/blobs';

export default async (req, context) => {
  // 1. Verifica Autenticazione (Basic Auth)
  const authHeader = req.headers.get('authorization');
  const user = process.env.STATS_USER;
  const pass = process.env.STATS_PASSWORD;

  if (!user || !pass) {
    return new Response('Configurazione server incompleta (variabili d\'ambiente mancanti).', { status: 500 });
  }

  const expectedAuth = 'Basic ' + Buffer.from(`${user}:${pass}`).toString('base64');
  if (authHeader !== expectedAuth) {
    return new Response('Accesso negato', {
      status: 401,
      headers: { 'WWW-Authenticate': 'Basic realm="Area Riservata"' },
    });
  }

  // 2. Recupero del Riepilogo Aggregato
  try {
    const store = getStore({ name: 'page-views' });
    
    // Leggiamo il blob di riepilogo creato dalla funzione pianificata (update-stats.mjs)
    let summary = await store.get('__summary__', { type: 'json' });

    // Se il riepilogo non esiste ancora, mostriamo un messaggio di attesa
    if (!summary) {
      if (req.url && new URL(req.url).searchParams.get('format') === 'json') {
        return new Response(JSON.stringify({ statsData: [], lastUpdate: null }), {
          status: 200,
          headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store, max-age=0' },
        });
      }
      return new Response(generateHTML([], null), {
        status: 200,
        headers: { 'Content-Type': 'text/html' },
      });
    }

    // Se è stato richiesto il formato JSON
    if (req.url && new URL(req.url).searchParams.get('format') === 'json') {
      return new Response(JSON.stringify(summary), {
        status: 200,
        headers: { 
          'Content-Type': 'application/json',
          'Cache-Control': 'no-store, max-age=0'
        },
      });
    }

    // 3. Rendering con i dati del riepilogo
    const html = generateHTML(summary.statsData, summary.lastUpdate);
    
    return new Response(html, {
      status: 200,
      headers: { 
        'Content-Type': 'text/html',
        'Cache-Control': 'no-store, max-age=0'
      },
    });

  } catch (error) {
    console.error('Errore critico durante la generazione delle statistiche:', error);
    return new Response(`Errore server: ${error.message}`, { status: 500 });
  }
};
