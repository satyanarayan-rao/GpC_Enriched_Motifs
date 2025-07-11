import sys


prev = sys.stdin.readline()
for n in  sys.stdin:
    prev_idx, prev_base_idx, prev_base_val = prev.strip().split("\t")
    next_idx, next_base_idx, next_base_val = n.strip().split("\t") 
    if prev_base_idx == "2" and next_base_idx  == "1": 
        print ("\t".join (map(str, [prev_idx, next_idx, "G", "C", prev_base_val, next_base_val]))) 
        prev = n 
    else:
        prev = n 
