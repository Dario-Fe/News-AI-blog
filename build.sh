#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- STARTING BUILD PROCESS ---"

# 1. Ensure the main output directory exists
echo "1. Ensuring dist directory exists..."
mkdir -p dist

# 2. Copy site-wide static files (like form definitions)
echo "2. Copying site-wide static files..."
cp forms.html dist/forms.html

# 3. Build the site for each language
echo "3. Building site for each language..."
for lang in it en es fr de; do
  echo "--- Starting build for $lang ---"
  python build.py --lang "$lang"
done

# 4. Generate master files (sitemap, robots.txt, root redirect)
echo "4. Generating master files..."
python build.py --master-files

echo "--- BUILD PROCESS COMPLETE ---"
