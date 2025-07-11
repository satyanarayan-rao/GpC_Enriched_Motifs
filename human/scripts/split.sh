#!/bin/bash
# $1 : label: {hocomoco,jaspar}
src_file=`cat label_file_map.tsv | awk '$1==v' v=$1 | awk '{print $NF}'`
mkdir -p individual_${1}
cat all_tf_list_${1}.tsv |  while read tf
do 
    awk -v tf=" ${tf}_" '$0 ~ tf, /URL/' $src_file | cat base.txt -   > individual_${1}/${tf}.meme
done 
