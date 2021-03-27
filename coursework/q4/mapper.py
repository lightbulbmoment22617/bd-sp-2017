#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()

    # skip first line
    if ("Date/Time," in words):
        continue
    else:
        # (hour, power)
        print("%s\t%s" % (words[1][:2], words[9][:-1]))
