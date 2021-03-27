#!usr/bin/env python3
import sys

current_day = None
current_prox_ids = []

for line in sys.stdin:
    line = line.strip()

    # output from combiner is (day, [list of prox_ids])
    day, prox_ids = line.split("\t", 1)
    prox_ids = prox_ids.split()

    if (day == current_day):
        current_prox_ids += prox_ids
    else:
        if (current_day is not None):
             # use python sets to quickly get the number of unique items
             print("%s\t%s" % (current_day, len(set(current_prox_ids))))

        current_day = day
        current_prox_ids = prox_ids

if (current_day is not None):
    print("%s\t%s" % (current_day, len(set(current_prox_ids))))
