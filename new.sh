#!/bin/bash
# Usage: ./new.sh 01 [py]
DAY=$1
LANG=${2:-py}
EXT=$LANG

# Handle extension mapping
if [ "$LANG" == "kotlin" ]; then EXT="main.kts"; fi
if [ "$LANG" == "js" ]; then EXT="js"; fi

mkdir -p day$DAY
cp templates/template.$EXT day$DAY/solution.$EXT
touch inputs/day$DAY.txt
code day$DAY/solution.$EXT
echo "Created day$DAY/solution.$EXT"