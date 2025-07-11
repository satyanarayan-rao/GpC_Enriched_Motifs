import sys
from collections import defaultdict
import numpy as np
cnt = 1
for line in sys.stdin:
    l_items = [float (i) for i in  line.strip().split("\t")]
    idx = np.argmax(l_items)
    val = np.max (l_items)
    print ("\t".join (map(str, [cnt, idx, val])))
    cnt = cnt + 1 
