import os

with open('build.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if 'temp_html = temp_html.replace("{{subscribe_link_text}}", TRANSLATIONS["subscribe"].get(lang, TRANSLATIONS["subscribe"]["it"]))' in line:
        indent = line[:line.find('temp_html')]
        # Determine depth based on current function context (very simple check)
        # Author pages use depth 2, others use 1.
        depth = "1"
        # Search backwards for function name
        for prev in reversed(new_lines):
            if 'def generate_author_pages' in prev:
                depth = "2"
                break
            if 'def generate_' in prev:
                break

        new_lines.append(f'{indent}temp_html = temp_html.replace("{{{{lang}}}}", lang)\n')
        new_lines.append(f'{indent}temp_html = temp_html.replace("{{{{depth}}}}", "{depth}")\n')
        new_lines.append(f'{indent}temp_html = temp_html.replace("{{{{search_placeholder}}}}", TRANSLATIONS["search"]["placeholder"].get(lang, TRANSLATIONS["search"]["placeholder"]["it"]))\n')
        new_lines.append(f'{indent}temp_html = temp_html.replace("{{{{search_label}}}}", TRANSLATIONS["search"]["label"].get(lang, TRANSLATIONS["search"]["label"]["it"]))\n')
        new_lines.append(f'{indent}temp_html = temp_html.replace("{{{{search_no_results}}}}", TRANSLATIONS["search"]["no_results"].get(lang, TRANSLATIONS["search"]["no_results"]["it"]))\n')

with open('build.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
