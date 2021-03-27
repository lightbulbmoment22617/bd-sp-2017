#!usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    # output from combiner is (timestamp, [list of prox_ids])
    day, prox_ids = line.split("\t", 1)
    prox_ids = prox_ids.split()

    # use python's set to quickly get unique ids
    unique_ids = len(set(prox_ids))
    print("%s\t%s" % (day, unique_ids))
