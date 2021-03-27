#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    # skip first line
    if ("prox-id," in words):
        continue
    else:
        # (timestamp, id)
        print("%s\t%s" % (words[0], words[3]))
