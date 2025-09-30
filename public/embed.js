document.addEventListener('DOMContentLoaded', function() {
    const embedContainer = document.getElementById('aitalk-latest-post');

    if (embedContainer) {
        const lang = embedContainer.dataset.lang || 'it';
        const siteUrl = embedContainer.dataset.url || 'https://aitalk.it';
        const jsonUrl = `${siteUrl}/${lang}/articles.json`;
        const placeholderImage = `${siteUrl}/logo_vn_ia.png`;
        
        const translations = {
            it: 'Leggi su AITalk &rarr;',
            en: 'Read on AITalk &rarr;',
            es: 'Leer en AITalk &rarr;',
            fr: 'Lire sur AITalk &rarr;',
            de: 'Lesen Sie auf AITalk &rarr;'
        };
        const readMoreText = translations[lang] || translations['it'];

        fetch(jsonUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Network response was not ok: ${response.statusText}`);
                }
                return response.json();
            })
            .then(articles => {
                if (articles && articles.length > 0) {
                    const latestArticle = articles[0]; // The JSON is sorted newest to oldest
                    const articleUrl = `${siteUrl}/${lang}/${latestArticle.path}`;

                    let imageHtml = '';
                    if (latestArticle.image_paths && latestArticle.image_paths.thumb_jpeg) {
                        const imageUrl = `${siteUrl}/${lang}/${latestArticle.image_paths.thumb_jpeg}`;
                        imageHtml = `<img src="${imageUrl}" alt="${latestArticle.title}" style="width: 100%; height: auto; border-radius: 8px 8px 0 0; object-fit: cover; border-bottom: 1px solid #eee;">`;
                    } else {
                         imageHtml = `<img src="${placeholderImage}" alt="AITalk" style="width: 100%; height: auto; border-radius: 8px 8px 0 0; object-fit: cover; border-bottom: 1px solid #eee;">`;
                    }
                    
                    const embedHtml = `
                        <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; max-width: 400px; margin: 20px auto; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                            <a href="${articleUrl}" target="_blank" rel="noopener" style="text-decoration: none; color: inherit; display: block;">
                                ${imageHtml}
                            </a>
                            <div style="padding: 15px;">
                                <h3 style="margin: 0 0 10px; font-size: 1.2em; color: #1c1e21;">
                                    <a href="${articleUrl}" target="_blank" rel="noopener" style="text-decoration: none; color: inherit;">${latestArticle.title}</a>
                                </h3>
                                <p style="margin: 0 0 15px; font-size: 0.9em; color: #606770; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden;">
                                    ${latestArticle.summary}
                                </p>
                                <a href="${articleUrl}" target="_blank" rel="noopener" style="display: inline-block; padding: 8px 15px; background-color: #0056b3; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; font-size: 0.9em;">
                                    ${readMoreText}
                                </a>
                            </div>
                        </div>
                    `;
                    embedContainer.innerHTML = embedHtml;
                } else {
                    throw new Error("No articles found in the JSON file.");
                }
            })
            .catch(error => {
                console.error('Error fetching latest post for AITalk embed:', error);
                embedContainer.innerHTML = '<p style="font-family: sans-serif; color: #666;">Impossibile caricare l\'ultimo articolo di AITalk.</p>';
            });
    }
});