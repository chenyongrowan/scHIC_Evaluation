#!/bin/bash
declare -A resolution
resolution[1Mb]=1000000
resolution[500kb]=500000
resolution[250kb]=250000
resolution[100kb]=100000
resolution[50kb]=50000

for r in "${!resolution[@]}"; do 
    mkdir "./"$r    
    echo "Key: $r, Value: ${resolution[$r]}"
    for file in ./*.txt; do 
        fileout=$(echo "$file" | awk -v r="$r" -v res="${resolution[$r]}" 'BEGIN{FS="[./]"; OFS="_"}{print "./"r"/"$2".cool"}')
        echo "File out: $fileout"
        cooler cload pairs -c1 2 -p1 3 -c2 5 -p2 6 --assembly mm10 ../../../mm10_RefGenome/mm10.chrom.sizes:${resolution[$r]} "$file" "$fileout"
    done
done
