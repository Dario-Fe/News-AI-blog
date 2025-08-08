#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- STARTING BUILD PROCESS ---"

# 1. Clean and create the main output directory
echo "1. Cleaning previous build..."
if [ -d "dist" ]; then rm -r dist; fi
mkdir dist

# 2. Copy site-wide static files (like form definitions)
echo "2. Copying site-wide static files..."
cp forms.html dist/forms.html

# 3. Build the site for each language
echo "2. Building site for each language..."
for lang in it en es; do
  echo "--- Building for $lang ---"
  python3 build.py --lang "$lang"
done

# 4. Create the root redirect file
echo "4. Creating root redirect..."
python3 -c "from build import create_root_redirect; create_root_redirect()"

echo "--- BUILD PROCESS COMPLETE ---"
