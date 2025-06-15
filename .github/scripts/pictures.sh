#!/usr/bin/env bash
# Gewnerate webp images from jpg/png files for responsive images.
find public/ -path public/icon -prune -o -path public/banner -prune -o -type f \( -iname '*.jpg' -o -iname '*.png' \) -print | while read -r f; do
    for w in 320 640 1024
    do
        webp="${f%.*}-$w.webp"
        echo "Generating $webp"
        magick "$f" -resize "${w}x" "$webp"

        avif="${f%.*}-$w.avif"
        echo "Generating $avif"
        magick "$f" -resize "${w}x" "$avif"
    done
done
