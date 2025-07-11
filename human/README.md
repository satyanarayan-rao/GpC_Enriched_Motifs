# Generating a list of TFs from MEME file

```
grep ^MOTIF HOCOMOCOv11_core_HUMAN_mono_meme_format.meme  | awk '{print $NF}'  | awk -F'_' '{print $1}' | sort | uniq  > all_tf_list.tsv
mkdir -p individual
sh scripts/split.sh
ls individual/*.meme > meme_list.tsv

sh scripts/run_for_all.sh  meme_list.tsv > gpc_info.tsv

awk '$(NF-1)>0.5 && ($NF + $(NF-1)) > 1' gpc_info.tsv  > filtered.tsv

awk '{print $1}' filtered.tsv | sort | uniq > tf_with_gpc_motif.tsv 
```

