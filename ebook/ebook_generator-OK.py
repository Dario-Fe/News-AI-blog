import os
import re
import sys
import frontmatter
import markdown2
from datetime import datetime
from collections import defaultdict
from reportlab.platypus import SimpleDocTemplate, Image, PageBreak, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from PIL import Image as PILImage
from html.parser import HTMLParser
from PyPDF2 import PdfWriter, PdfReader

# --- Gestione Robusta dei Percorsi ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
# ------------------------------------

# --- Parser da HTML a ReportLab Story ---
class HTMLToStoryParser(HTMLParser):
    def __init__(self, styles, article_base_path=""):
        super().__init__()
        self.styles = styles
        self.article_base_path = article_base_path
        self.story = []
        self.text_fragments = []
        self.current_style_stack = [self.styles['BodyCustom']]
        self.list_styles = [] 
        self.list_items = []
        self.in_li = False

    def current_style(self):
        return self.current_style_stack[-1]

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'p': pass
        elif tag == 'h1': self.current_style_stack.append(self.styles['H1Custom'])
        elif tag == 'h2': self.current_style_stack.append(self.styles['H2Custom'])
        elif tag == 'strong' or tag == 'b': self.text_fragments.append('<b>')
        elif tag == 'em' or tag == 'i': self.text_fragments.append('<i>')
        elif tag == 'ul': self.list_styles.append('ul')
        elif tag == 'ol': self.list_styles.append('ol')
        elif tag == 'li': 
            self.in_li = True
            self.text_fragments = []
        elif tag == 'img' and 'src' in attrs:
            self.handle_image(attrs['src'])

    def handle_image(self, src):
        # Costruisce il percorso assoluto dell'immagine
        image_path = os.path.join(self.article_base_path, src)
        if os.path.exists(image_path):
            try:
                # Aggiunge un po' di spazio prima e dopo l'immagine
                self.story.append(Spacer(1, 6*mm))
                # Logica di ridimensionamento proporzionale
                max_width = 150 * mm
                max_height = 180 * mm
                pil_img = PILImage.open(image_path)
                original_width, original_height = pil_img.size
                ratio = min(max_width / original_width, max_height / original_height)
                new_width = original_width * ratio
                new_height = original_height * ratio
                
                img = Image(image_path, width=new_width, height=new_height, hAlign='CENTER')
                self.story.append(img)
                self.story.append(Spacer(1, 6*mm))
            except Exception as e:
                print(f"Attenzione: Impossibile processare l'immagine interna {image_path}. Errore: {e}")

    def handle_endtag(self, tag):
        if tag in ['p', 'h1', 'h2']:
            if self.text_fragments:
                self.story.append(Paragraph("".join(self.text_fragments), self.current_style()))
                self.text_fragments = []
            if tag in ['h1', 'h2']: self.current_style_stack.pop()
        elif tag == 'strong' or tag == 'b': self.text_fragments.append('</b>')
        elif tag == 'em' or tag == 'i': self.text_fragments.append('</i>')
        elif tag in ['ul', 'ol']:
            if self.list_items:
                list_type = self.list_styles.pop()
                bullet = 'bullet' if list_type == 'ul' else '1'
                list_flowable = ListFlowable(self.list_items, bulletType=bullet, spaceBefore=10, spaceAfter=10)
                self.story.append(list_flowable)
                self.list_items = []
        elif tag == 'li':
            if self.text_fragments:
                item_paragraph = Paragraph("".join(self.text_fragments), self.styles['BodyCustom'])
                self.list_items.append(ListItem(item_paragraph))
            self.in_li = False
            self.text_fragments = []
        elif tag == 'br': self.text_fragments.append('<br/>')

    def handle_data(self, data):
        if data.strip(): self.text_fragments.append(data.strip())

def html_to_story(html_content, styles, article_base_path=""):
    html_content = re.sub(r'</?(html|body|head|meta|title)>', '', html_content)
    parser = HTMLToStoryParser(styles, article_base_path)
    parser.feed(f"<p>{html_content}</p>") 
    return parser.story
# -----------------------------------------

def get_user_input():
    if len(sys.argv) != 3:
        print("Uso: python ebook_generator.py <start_range> <end_range>")
        sys.exit(1)
    try:
        start_range = int(sys.argv[1])
        end_range = int(sys.argv[2])
        if start_range <= 0 or end_range <= 0 or end_range < start_range:
            raise ValueError("Gli intervalli devono essere numeri positivi e l'inizio non può superare la fine.")
        return start_range, end_range
    except ValueError as e:
        print(f"Errore: Argomenti non validi. {e}")
        sys.exit(1)

def find_and_parse_articles(start, end):
    articles_path = os.path.join(REPO_ROOT, 'articoli')
    parsed_articles = []
    print(f"\nRicerca articoli in '{articles_path}'...")
    for folder_name in sorted(os.listdir(articles_path)):
        match = re.match(r'^(\d+)', folder_name)
        if not match: continue
        article_num = int(match.group(1))
        if start <= article_num <= end:
            article_path = os.path.join(articles_path, folder_name)
            if not os.path.isdir(article_path): continue
            # --- Logica per Articoli Multi-Parte ---
            all_md_files = [f for f in os.listdir(article_path) if f.endswith('.md') and not re.search(r'_[a-z]{2}\.md$', f)]
            
            # Funzione di ordinamento personalizzata
            def sort_key(filename):
                order = {"prima": 1, "seconda": 2, "terza": 3, "quarta": 4, "quinta": 5}
                for key, value in order.items():
                    if key in filename.lower():
                        return value
                return 99 # File senza numero di puntata vengono messi alla fine
            
            sorted_parts = sorted(all_md_files, key=sort_key)

            if sorted_parts:
                try:
                    # Carica il primo file per estrarre i metadati principali
                    first_file_path = os.path.join(article_path, sorted_parts[0])
                    with open(first_file_path, 'r', encoding='utf-8') as f:
                        first_post = frontmatter.load(f)

                    # Estrae titolo, immagine e metadati dal PRIMO file
                    title_match = re.search(r'^\s*#\s(.+)', first_post.content, re.MULTILINE)
                    title = title_match.group(1).strip() if title_match else "Senza Titolo"
                    image_match = re.search(r'!\[.*\]\((.+)\)', first_post.content)
                    image_path = os.path.join(article_path, image_match.group(1)) if image_match else None
                    date_obj = first_post.metadata.get('date', datetime.now().date())
                    if isinstance(date_obj, str):
                        date_obj = datetime.strptime(date_obj, '%Y-%m-%d').date()

                    # Processa ogni parte separatamente e le salva in una lista
                    content_parts = []
                    for i, part_name in enumerate(sorted_parts):
                        file_path = os.path.join(article_path, part_name)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            post = frontmatter.load(f)
                            content = post.content
                            
                            # Dalla prima parte, rimuove il titolo H1 e l'immagine di copertina
                            if i == 0:
                                content = re.sub(r'^\s*#\s' + re.escape(title) + r'\s*\n', '', content, count=1)
                                if image_path:
                                    image_filename = os.path.basename(image_path)
                                    content = re.sub(r'!\[.*\]\(' + re.escape(image_filename) + r'\)\s*\n', '', content, count=1)
                            
                            content_parts.append(content.strip())
                    
                    article_data = {
                        'title': title,
                        'metadata': first_post.metadata,
                        'content_parts': content_parts, # Ora è una lista di puntate
                        'article_folder_path': article_path,
                        'image_path': image_path,
                        'date': date_obj
                    }
                    parsed_articles.append(article_data)
                except Exception as e:
                    print(f"Errore durante l'analisi della cartella {article_path}: {e}")
    return parsed_articles

def generate_content_pdf(articles, tocs, output_path, styles):
    """Genera il PDF con tutto il contenuto, esclusa la copertina."""
    doc = SimpleDocTemplate(output_path, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=25*mm, bottomMargin=25*mm)
    story = []
    
    for page_name in ['introduzione.md', 'il-libro.md', 'ringraziamenti.md']:
        page_path = os.path.join(REPO_ROOT, 'ebook/assets', page_name)
        if os.path.exists(page_path):
            with open(page_path, 'r', encoding='utf-8') as f:
                content = markdown2.markdown(f.read())
            story.extend(html_to_story(content, styles))
            story.append(PageBreak())
            
    for article in articles:
        story.append(Paragraph(article['title'], styles['H1Custom']))
        if article['image_path'] and os.path.exists(article['image_path']):
            story.append(Spacer(1, 12*mm))
            try:
                max_width = 150 * mm
                max_height = 180 * mm
                pil_img = PILImage.open(article['image_path'])
                original_width, original_height = pil_img.size
                ratio = min(max_width / original_width, max_height / original_height)
                new_width = original_width * ratio
                new_height = original_height * ratio
                img = Image(article['image_path'], width=new_width, height=new_height, hAlign='CENTER')
                story.append(img)
            except Exception as e:
                print(f"Attenzione: Impossibile processare l'immagine {article['image_path']}. Errore: {e}")
            story.append(Spacer(1, 12*mm))
        
        # Itera su ogni parte dell'articolo e aggiunge un PageBreak tra di esse
        num_parts = len(article['content_parts'])
        for i, part_content in enumerate(article['content_parts']):
            html_content = markdown2.markdown(part_content)
            story.extend(html_to_story(html_content, styles, article['article_folder_path']))
            
            # Aggiunge un'interruzione di pagina se non è l'ultima parte
            if i < num_parts - 1:
                story.append(PageBreak())

        # Aggiunge un'interruzione di pagina alla fine di tutto l'articolo
        story.append(PageBreak())

    # Aggiunge la pagina della biografia prima degli indici
    bio_path = os.path.join(REPO_ROOT, 'ebook/assets/biografia.md')
    if os.path.exists(bio_path):
        with open(bio_path, 'r', encoding='utf-8') as f:
            content = markdown2.markdown(f.read())
        story.extend(html_to_story(content, styles))
        story.append(PageBreak())
    
    story.extend(tocs)
    doc.build(story)

def generate_cover_pdf(cover_path, output_path):
    """Genera un PDF di una sola pagina con la copertina."""
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawImage(cover_path, 0, 0, width=A4[0], height=A4[1])
    c.save()

def merge_pdfs(cover_pdf, content_pdf, final_pdf):
    """Unisci il PDF della copertina con quello del contenuto."""
    pdf_writer = PdfWriter()
    
    cover_reader = PdfReader(cover_pdf)
    pdf_writer.add_page(cover_reader.pages[0])
    
    content_reader = PdfReader(content_pdf)
    for page in content_reader.pages:
        pdf_writer.add_page(page)
        
    with open(final_pdf, 'wb') as out:
        pdf_writer.write(out)

def generate_tocs_reportlab(articles, styles):
    print("\nGenerazione degli indici...")
    story = []
    story.append(Paragraph("Indice Cronologico", styles['H1Custom']))
    story.append(Spacer(1, 8*mm))
    sorted_by_date = sorted(articles, key=lambda x: x['date'])
    for article in sorted_by_date:
        story.append(Paragraph(f'- {article["title"]} ({article["date"].strftime("%d/%m/%Y")})', styles['TocCustom']))
    story.append(PageBreak())
    
    story.append(Paragraph("Indice per Tag", styles['H1Custom']))
    story.append(Spacer(1, 8*mm))
    tags_dict = defaultdict(list)
    for article in articles:
        for tag in article['metadata'].get('tags', []):
            tags_dict[tag].append(article)
    
    for tag in sorted(tags_dict.keys()):
        story.append(Paragraph(tag.upper(), styles['H2Custom']))
        for article in sorted(tags_dict[tag], key=lambda x: x['date']):
            story.append(Paragraph(f'- {article["title"]}', styles['TocCustom']))
        story.append(Spacer(1, 6*mm))
    return story

def main():
    output_dir = os.path.join(REPO_ROOT, 'ebook/output')
    os.makedirs(output_dir, exist_ok=True)
    
    print("--- Generatore di Ebook ---")
    start, end = get_user_input()
    articles = find_and_parse_articles(start, end)
    
    if not articles:
        print("\nNessun articolo trovato. Uscita.")
        return
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='H1Custom', parent=styles['h1'], fontSize=24, leading=28, spaceAfter=10, alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='H2Custom', parent=styles['h2'], fontSize=18, leading=22, spaceAfter=8))
    styles.add(ParagraphStyle(name='BodyCustom', parent=styles['Normal'], fontSize=12, leading=16, spaceAfter=6))
    styles.add(ParagraphStyle(name='TocCustom', parent=styles['Normal'], fontSize=12, leading=16, spaceAfter=2, leftIndent=10))

    tocs = generate_tocs_reportlab(articles, styles)
    
    cover_path = os.path.join(REPO_ROOT, 'ebook/assets/copertina.jpg')
    final_pdf_path = os.path.join(output_dir, 'ebook.pdf')
    cover_temp_pdf = os.path.join(output_dir, 'temp_cover.pdf')
    content_temp_pdf = os.path.join(output_dir, 'temp_content.pdf')

    try:
        print("\nGenerazione del PDF...")
        if os.path.exists(cover_path):
            generate_cover_pdf(cover_path, cover_temp_pdf)
        
        generate_content_pdf(articles, tocs, content_temp_pdf, styles)
        
        if os.path.exists(cover_temp_pdf):
            merge_pdfs(cover_temp_pdf, content_temp_pdf, final_pdf_path)
        else:
            os.rename(content_temp_pdf, final_pdf_path)
            
        print(f"\n--- SUCCESSO! ---")
        print(f"Ebook generato e salvato in: {final_pdf_path}")

    except Exception as e:
        print(f"\n--- ERRORE CRITICO ---")
        print(f"Si è verificato un errore imprevisto: {e}")
    
    finally:
        if os.path.exists(cover_temp_pdf): os.remove(cover_temp_pdf)
        if os.path.exists(content_temp_pdf): os.remove(content_temp_pdf)

if __name__ == "__main__":
    main()
