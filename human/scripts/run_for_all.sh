#!/bin/bash
# $1 : a file containing a list of meme file paths, one in each line. See 
cat $1 |  while read meme_file
do
    name=`echo $meme_file | awk -F'/' '{print $NF}' | awk -F'.' '{print $1}'`
    tail -n +12 $meme_file | head -n -1 | python scripts/get_max_at_each_pos.py | python scripts/scan_for_gc.py | awk '{print v"\t"$0}' v=$name 
done 
