#!/usr/bin/env bash
# Add index files to content subdirectories if they contain Markdown files.
find content/ -type d | while read -r dir; do
    if find "$dir" -maxdepth 1 -type f -name '*.md' | grep -q .; then
        index_file="$dir/_index.md"
        if [ ! -f "$index_file" ]; then
            echo "Creating $index_file"
            echo "+++" > "$index_file"
            echo "+++" >> "$index_file"
        fi
    fi
done
