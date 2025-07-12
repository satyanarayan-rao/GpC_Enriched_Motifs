import sys
from collections import defaultdict
import gzip
import re
import pickle

pkl_dict = pickle.load(open(sys.argv[1], "rb"))

for line in sys.stdin:
    d_loc = [m.start() for m in re.finditer("\t", line)]
    k = None
    if len(d_loc)==0:
        k = line.strip()
    else:
        k = line[0:d_loc[0]]
    if k in pkl_dict:
        to_write = line.strip() + "\t" + pkl_dict[k]
        print (to_write)
    else:
        continue
