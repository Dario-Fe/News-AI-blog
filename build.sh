#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

echo "--- STARTING BUILD PROCESS ---"

# 1. Clean and create the main output directory
echo "1. Cleaning previous build..."
if [ -d "dist" ]; then rm -r dist; fi
mkdir dist

# 2. Copy static assets to the root of the output directory
# We run this as a separate Python call to keep concerns separate.
echo "2. Copying static assets..."
python3 -c "from build import copy_static_assets; copy_static_assets('dist')"

# 3. Build the site for each language
echo "3. Building site for each language..."
for lang in it en es; do
  echo "--- Building for $lang ---"
  python3 build.py --lang "$lang"
  python3 -c "from build import generate_local_pages; generate_local_pages('dist/$lang', '$lang')"
done

# 4. Create the root redirect file
echo "4. Creating root redirect..."
python3 -c "from build import create_root_redirect; create_root_redirect()"

echo "--- BUILD PROCESS COMPLETE ---"
