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
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
from html.parser import HTMLParser

# --- Gestione Robusta dei Percorsi ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
# ------------------------------------

# --- Parser da HTML a ReportLab Story ---
class HTMLToStoryParser(HTMLParser):
    def __init__(self, styles):
        super().__init__()
        self.styles = styles
        self.story = []
        self.text_fragments = []
        self.current_style_stack = [self.styles['BodyCustom']]
        self.list_styles = [] 
        self.list_items = []
        self.in_li = False

    def current_style(self):
        return self.current_style_stack[-1]

    def handle_starttag(self, tag, attrs):
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

def html_to_story(html_content, styles):
    html_content = re.sub(r'</?(html|body|head|meta|title)>', '', html_content)
    parser = HTMLToStoryParser(styles)
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
            main_md_file = None
            for file_name in os.listdir(article_path):
                if file_name.endswith('.md') and not re.search(r'_[a-z]{2}\.md$', file_name):
                    main_md_file = file_name
                    break
            if main_md_file:
                file_path = os.path.join(article_path, main_md_file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        post = frontmatter.load(f)
                        title_match = re.search(r'^\s*#\s(.+)', post.content, re.MULTILINE)
                        title = title_match.group(1).strip() if title_match else "Senza Titolo"
                        image_match = re.search(r'!\[.*\]\((.+)\)', post.content)
                        image_path = os.path.join(article_path, image_match.group(1)) if image_match else None
                        date_obj = post.metadata.get('date', datetime.now().date())
                        if isinstance(date_obj, str):
                            date_obj = datetime.strptime(date_obj, '%Y-%m-%d').date()
                        
                        content = re.sub(r'^\s*#\s.+\n', '', post.content)
                        content = re.sub(r'!\[.*\]\(.+\)\n', '', content)
                        
                        article_data = {
                            'title': title,
                            'metadata': post.metadata,
                            'content': content.strip(),
                            'image_path': image_path,
                            'date': date_obj
                        }
                        parsed_articles.append(article_data)
                except Exception as e:
                    print(f"Errore durante l'analisi del file {file_path}: {e}")
    return parsed_articles

def generate_pdf_final(cover_path, articles, tocs, output_path, styles):
    print("\nGenerazione del PDF con ReportLab...")
    try:
        doc = SimpleDocTemplate(output_path, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=25*mm, bottomMargin=25*mm)
        story = []
        
        # Funzione per disegnare la copertina a piena pagina
        def draw_cover(canvas, doc):
            canvas.saveState()
            canvas.drawImage(cover_path, 0, 0, width=A4[0], height=A4[1])
            canvas.restoreState()
        
        on_first_page_hook = None
        if os.path.exists(cover_path):
            on_first_page_hook = draw_cover
            story.append(PageBreak()) # Inizia il contenuto dalla seconda pagina

        # Carica le nuove pagine introduttive nell'ordine specificato
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
            
            html_content = markdown2.markdown(article['content'])
            story.extend(html_to_story(html_content, styles))
            story.append(PageBreak())
        
        story.extend(tocs)
        doc.build(story, onFirstPage=on_first_page_hook) # Applica la funzione per la copertina
        print(f"\n--- SUCCESSO! ---")
        print(f"Ebook generato e salvato in: {output_path}")

    except Exception as e:
        print(f"\n--- ERROre CRITICO ---")
        print(f"Si è verificato un errore imprevisto: {e}")

def generate_tocs_reportlab(articles, styles):
    print("\nGenerazione degli indici...")
    story = []
    story.append(Paragraph("Indice Cronologico", styles['H1Custom']))
    story.append(Spacer(1, 8*mm))
    sorted_by_date = sorted(articles, key=lambda x: x['date'])
    for article in sorted_by_date:
        story.append(Paragraph(f'{article["title"]} ({article["date"].strftime("%d/%m/%Y")})', styles['TocCustom']))
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
    
    output_pdf_path = os.path.join(output_dir, 'ebook.pdf')
    cover_path = os.path.join(REPO_ROOT, 'ebook/assets/copertina.jpg')
    generate_pdf_final(cover_path, articles, tocs, output_pdf_path, styles)

if __name__ == "__main__":
    main()
