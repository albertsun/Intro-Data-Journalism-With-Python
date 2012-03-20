#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

findhours = re.compile(r'(\d{1,2}(:\d\d)?)-((\d{1,2}(:\d\d)?)(([AP]M)|NOON))')
starts = []
ends = []


# looping over every file in the directory
for filename in os.listdir("pennregistrar/"):
    f = open("pennregistrar/"+filename, "r")
    for line in f:
        m = findhours.search(line)
        if m:
            x = m.groups()
            start = x[0]
            end = x[2]
            starts.append(start)
            ends.append(end)
            print start,end
    f.close()

print "found %(count)d total class times" % { "count": len(starts) }    

# dividing up the classes we've found into different timeslots to count them
timeslots = {} #defaultdict(int)
for i in range(len(starts)):
	key = starts[i]+"-"+ends[i]
	if timeslots.has_key(key):
		timeslots[key] += 1
	else:
		timeslots[key] = 1


sorted_timeslots = sorted(timeslots.items(), key=lambda x:x[1], reverse=True)
for time in sorted_timeslots:
	print time


