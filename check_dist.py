import os
import re

def check_file(path, expected_depth):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, 'r') as f:
        content = f.read()
        depth_match = re.search(r"parseInt\('([^']*)'", content)
        lang_match = re.search(r"lang: '([^']*)'", content)
        search_match = re.search(r"placeholder: '([^']*)'", content)

        depth = depth_match.group(1) if depth_match else "NOT FOUND"
        lang = lang_match.group(1) if lang_match else "NOT FOUND"

        if depth == expected_depth:
            print(f"OK: {path} has depth {depth}")
        else:
            print(f"FAIL: {path} has depth {depth}, expected {expected_depth}")

        print(f"  Lang: {lang}")

check_file('dist/it/index.html', '1')
check_file('dist/it/recursivemas.html', '1')
check_file('dist/it/authors/dario-ferrero.html', '2')
check_file('dist/it/cookie.html', '1')
