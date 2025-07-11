# Generating a list of TFs from MEME file

## For HOCOMOCO motif file

```
grep ^MOTIF HOCOMOCOv11_core_HUMAN_mono_meme_format.meme  | awk '{print $NF}'  | awk -F'_' '{print $1}' | sort | uniq  > all_tf_list_hocomoco.tsv 

sh scripts/split.sh hocomoco
ls individual_hocomoco/*.meme > meme_list_hocomoco.tsv

sh scripts/run_for_all.sh  meme_list_hocomoco.tsv > gpc_info_hocomoco.tsv

awk '$(NF-1)>0.5 && ($NF + $(NF-1)) > 1' gpc_info_hocomoco.tsv  > filtered_hocomoco.tsv

awk '{print $1}' filtered_hocomoco.tsv | sort | uniq > tf_with_gpc_motif_hocomoco.tsv 

```
## For JASPAR file

```
grep MOTIF 20250525090713_JASPAR2024_combined_matrices_981783_meme.txt | awk '{print $3}' | tr "." "\t" | awk '{print $3"\t"$1"."$2}' | grep -v "::" > all_tf_list_jaspar.tsv

sh scripts/split.sh jaspar
ls individual_jaspar/*.meme > meme_list_jaspar.tsv

sh scripts/run_for_all.sh  meme_list_jaspar.tsv > gpc_info_jaspar.tsv

awk '$(NF-1)>0.5 && ($NF + $(NF-1)) > 1' gpc_info_jaspar.tsv  > filtered_jaspar.tsv

awk '{print $1}' filtered_jaspar.tsv | sort | uniq > tf_with_gpc_motif_jaspar.tsv 

```


## Combine JASPAR and HOCOMOCO information

```
python scripts/combine_hoco_jas.py tf_with_gpc_motif_hocomoco.tsv tf_with_gpc_motif_jaspar.tsv > combined_tf_motifs_with_gpc.tsv
```

