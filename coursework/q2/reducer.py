#!/usr/bin/env python3
import sys

current_fz = None
current_count = 0
max_fz = None
max_count = 0

def update_max(current_count, current_fz):
    global max_fz, max_count
    if (current_count > max_count):
        max_count = current_count
        max_fz = current_fz

for line in sys.stdin:
    line = line.strip()

    # output from mapper is (floor zone, 1)
    fz, count = line.split("\t", 1)

    # check input validity
    try:
        count = int(count)
    except ValueError:
        continue

    if (fz == current_fz):
        # update the count of number of visits
        current_count += count
    else:
        if (current_fz is not None):
            update_max(current_count, current_fz)

        current_fz = fz
        current_count = count

# output final count
if (current_fz):
    update_max(current_count, current_fz)

print("%s\t%s" % (max_fz, max_count))
