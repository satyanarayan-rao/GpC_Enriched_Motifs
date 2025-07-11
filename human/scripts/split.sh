cat all_tf_list.tsv |  while read tf
do 
    awk -v tf=" ${tf}_" '$0 ~ tf, /URL/' HOCOMOCOv11_core_HUMAN_mono_meme_format.meme | cat base.txt -   > individual/${tf}.meme
done 
