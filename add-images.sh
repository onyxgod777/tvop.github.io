#!/data/data/com.termux/files/usr/bin/bash
# Add stock images to TVOP blog posts (mirrors Pi)

BLOGDIR="blog/posts"
IMGDIR="img"

declare -A IMG_MAP
IMG_MAP["432-connexion-phi-pi-alpha"]="sacred-geometry"
IMG_MAP["figu-plejaren-contact-report-251-pi-correction"]="space-universe"
IMG_MAP["golden-pi-identity"]="geometry-circle"
IMG_MAP["great-pyramid-golden-pi-encodes-earth-dimensions"]="great-pyramid"
IMG_MAP["harry-lear-measuring-pi"]="math-equations"
IMG_MAP["jain-108-jainpi-book-of-phi"]="nautilus-shell"
IMG_MAP["music-spheres-golden-ratio-harmonics"]="music-harmony"
IMG_MAP["phi-pi-research-001"]="math-equations"
IMG_MAP["phi-pi-research-002"]="math-equations"
IMG_MAP["physical-experiments-golden-pi-measurements"]="geometry-circle"
IMG_MAP["pi-gap-comparison-conventional-golden"]="geometry-circle"
IMG_MAP["pythagorean-triangle-proof"]="geometry-circle"
IMG_MAP["restoring-trigonometry-golden-pi-sine-function"]="trigonometry"
IMG_MAP["royal-cubit-phi-squared-pi-six-connection"]="great-pyramid"
IMG_MAP["source-map-30-references-golden-pi"]="sacred-geometry"
IMG_MAP["squaring-circle-golden-pi-geometric-proof"]="geometry-circle"
IMG_MAP["stefanides-golden-root-symmetries-engineering-golden-pi"]="math-equations"

cd /data/data/com.termux/files/home/workspace/tvop.github.io

for file in "$BLOGDIR"/*.html; do
    base=$(basename "$file" .html)
    img_base="${IMG_MAP[$base]}"
    
    if [ -z "$img_base" ]; then
        echo "SKIP $base — no image mapping"
        continue
    fi
    
    img_file="$IMGDIR/${img_base}.jpg"
    if [ ! -f "$img_file" ]; then
        echo "SKIP $base — missing $img_file"
        continue
    fi
    
    if grep -q '<img src="../../img/' "$file" || grep -q '<img src="img/' "$file"; then
        echo "SKIP $base — already has image"
        continue
    fi
    
    sed -i '/opacity:0.6;margin-bottom:30px/{n;a\<img src="../../img/'"${img_base}"'.jpg" alt="'"${base//-/ }"'" style="width:100%;max-width:720px;height:auto;border-radius:12px;margin:0 auto 24px;display:block;" />
}' "$file"
    
    echo "ADDED img to $base ($img_base.jpg)"
done

echo "Done with TVOP!"
