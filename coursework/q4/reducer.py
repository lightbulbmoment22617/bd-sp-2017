#!usr/bin/env python3
import sys

current_hour = None
current_total = 0
current_count = 0

for line in sys.stdin:
    line = line.strip()

    # output from combiner is (hour, [list of power measurements])
    hour, powers = line.split("\t", 1)
    powers = powers.split()

    if (hour == current_hour):
        current_total += sum([float(x) for x in powers])
        current_count += len(powers)
    else:
        if (current_hour is not None and current_count > 0):
             average = current_total / current_count
             print("%s\t%s" % (current_hour, average))

        current_hour = hour
        current_total = sum([float(x) for x in powers])
        current_count = len(powers)

if (current_hour is not None and current_count > 0):
    average = current_total / current_count
    print("%s\t%s" % (current_hour, average))
