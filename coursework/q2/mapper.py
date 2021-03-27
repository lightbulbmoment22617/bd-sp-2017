#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    # skip first line
    if ("prox-id," in words):
        continue
    else:
        # (floor zone, id)
        key = "%s %s" % (words[4], words[5])
        print("%s\t%s" % (key, 1))
