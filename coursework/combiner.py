#!/usr/bin/env python3
import sys

current_day = None
current_prox_ids = []

for line in sys.stdin:
    line = line.strip()

    # output from mapper is (timestamp, prox_id)
    day, prox_id = line.split("\t", 1)

    if (day == current_day):
        # add the id to the list of ids for this day
        current_prox_ids.append(prox_id)
    else:
        if (current_day):
            output = "%s\t" % current_day
            output += " ".join(map(str, current_prox_ids))
            print("%s\t%s" % (current_day, current_prox_ids))

        current_day = day
        current_prox_ids = [prox_id]

# output final day
if (current_day):
    output = "%s\t" % current_day
    output += " ".join(map(str, current_prox_ids))
    print(output)
