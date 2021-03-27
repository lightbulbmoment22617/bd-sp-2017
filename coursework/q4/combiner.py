#!/usr/bin/env python3
import sys

current_hour = None
current_powers = []

for line in sys.stdin:
    line = line.strip()

    # output from mapper is (hour, power)
    hour, power = line.split("\t", 1)

    if (hour == current_hour):
        # add the power to the list of powers for this hour
        current_powers.append(power)
    else:
        if (current_hour is not None):
            output = "%s\t" % current_hour
            output += " ".join(map(str, current_powers))
            print(output)

        current_hour = hour
        current_powers = [power]

# output final hour
if (current_hour is not None):
    output = "%s\t" % current_hour
    output += " ".join(map(str, current_powers))
    print(output)
