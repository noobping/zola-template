#!/usr/bin/env bash
# Add date to TOML front matter if it does not exist. Only for Markdown files, ignoring _*.md files.
find content/ -type f -name '*.md' ! -name '_*.md' | while read -r file; do
    if grep -q '^+++ *$' "$file"; then
        # Check if "date =" is already in front matter
        if ! awk '/^\+\+\+/{i++} i==1 && /^date *=/ {found=1; exit} END{exit !found}' "$file"; then
            echo "Adding date to $file"
            current_date=$(date +'%Y-%m-%d')
            # Insert 'date = "YYYY-MM-DD"' after the first +++ line
            awk -v date="$current_date" '
                BEGIN {added=0}
                /^\+\+\+ *$/ && !added {
                    print
                    print "date = \"" date "\""
                    added=1
                    next
                }
                {print}
            ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"
        fi
    fi
done
