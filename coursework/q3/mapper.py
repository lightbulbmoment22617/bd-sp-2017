#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    # skip first line
    if ("prox-id," in words):
        continue
    elif(words[0] == "2016-06-02"):
        # (id, 1)
        print("%s\t%s" % (words[3], 1))
