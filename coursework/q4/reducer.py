#!/usr/bin/env python3
import sys

current_hour = None
average_power = 0

for line in sys.stdin:
    line = line.strip()

    # output from mapper is (floor zone, 1)
    hour, power = line.split("\t", 1)

    # check input validity
    try:
        hour = int(hour)
        power = float(power)
    except ValueError:
        continue

    if (hour == current_hour):
        # update the average
        average_power = (average_power + power) / 2
    else:
        if (current_hour is not None):
            print("%s\t%s" % (current_hour, average_power))

        current_hour = hour
        average_power = power

# output final count
if (current_hour):
    print("%s\t%s" % (current_hour, average_power))
