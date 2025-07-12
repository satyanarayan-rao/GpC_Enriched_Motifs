import sys
import pickle
out_fp = open (sys.argv[1], "wb")
out_dict = {}
for line in sys.stdin:
    line_items = line.strip().split("\t")
    out_dict[line_items[0]] = "\t".join(line_items[1:])
pickle.dump(out_dict, out_fp)
out_fp.close()
