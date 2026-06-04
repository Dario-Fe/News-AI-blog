import re

with open('build.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Unified block of common replaces
common_replaces = """
        temp_html = temp_html.replace("{{lang}}", lang)
        temp_html = temp_html.replace("{{depth}}", str(depth))
        temp_html = temp_html.replace("{{search_placeholder}}", TRANSLATIONS["search"]["placeholder"].get(lang, TRANSLATIONS["search"]["placeholder"]["it"]))
        temp_html = temp_html.replace("{{search_label}}", TRANSLATIONS["search"]["label"].get(lang, TRANSLATIONS["search"]["label"]["it"]))
        temp_html = temp_html.replace("{{search_no_results}}", TRANSLATIONS["search"]["no_results"].get(lang, TRANSLATIONS["search"]["no_results"]["it"]))"""

# I will target each function's "base_data = get_base_template_data" call and insert BEFORE it
content = re.sub(r'( +)base_data = get_base_template_data\(depth=(\d).*?\)',
                 lambda m: f'{m.group(1)}depth = {m.group(2)}\n{common_replaces.replace("        ", m.group(1))}\n{m.group(0)}',
                 content)

# Special case for index page where depth is often 1
# (The regex above should handle it if it matches the pattern)

# Clean up index page view_more_text correctly
content = content.replace("temp_html = temp_html.replace(\"{{view_more_text}}\", view_more_text.replace(\"'\", \"\\\\'\"))",
                        "temp_html = temp_html.replace(\"{{view_more_text}}\", view_more_text.replace(\"'\", \"\\\\'\"))\n    temp_html = temp_html.replace(\"{{lang}}\", lang)\n    temp_html = temp_html.replace(\"{{depth}}\", \"1\")\n    temp_html = temp_html.replace(\"{{search_placeholder}}\", TRANSLATIONS[\"search\"][\"placeholder\"].get(lang, TRANSLATIONS[\"search\"][\"placeholder\"][\"it\"]))\n    temp_html = temp_html.replace(\"{{search_label}}\", TRANSLATIONS[\"search\"][\"label\"].get(lang, TRANSLATIONS[\"search\"][\"label\"][\"it\"]))\n    temp_html = temp_html.replace(\"{{search_no_results}}\", TRANSLATIONS[\"search\"][\"no_results\"].get(lang, TRANSLATIONS[\"search\"][\"no_results\"][\"it\"]))")

with open('build.py', 'w', encoding='utf-8') as f:
    f.write(content)
