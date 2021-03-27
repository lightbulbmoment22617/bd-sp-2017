#!/usr/bin/env python3
import sys

current_id = None
current_count = 0
max_id = None
max_count = 0

def update_max(current_count, current_id):
    global max_id, max_count
    if (current_count > max_count):
        max_count = current_count
        max_id = current_id

for line in sys.stdin:
    line = line.strip()

    # output from mapper is (floor zone, 1)
    new_id, count = line.split("\t", 1)

    # check input validity
    try:
        count = int(count)
    except ValueError:
        continue

    if (new_id == current_id):
        # update the count of number of visits
        current_count += count
    else:
        if (current_id):
            update_max(current_count, current_id)

        current_id = new_id
        current_count = count

# output final count
if (current_id):
    update_max(current_count, current_id)

print("%s\t%s" % (max_id, max_count))
