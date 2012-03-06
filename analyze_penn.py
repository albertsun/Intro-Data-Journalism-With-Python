#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re
from collections import defaultdict

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
timeslots = defaultdict(int)
for i in range(len(starts)):
    timeslots[starts[i]+"-"+ends[i]] += 1

#print timeslots.items()
print(sorted(timeslots.items(), key=lambda x:x[1], reverse=True)[:10])
