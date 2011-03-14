#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re
from collections import defaultdict
from pprint import pprint

findhours = re.compile(r'(\d{1,2}(:\d\d)?)-((\d{1,2}(:\d\d)?)(([AP]M)|NOON))')
starts = []
ends = []

def parsefile(f):
    save = False
    for line in f:
        if line.find("<pre>") > -1:
            save = True
        if (save == True):
            m = findhours.search(line)
            if m:
                x = m.groups()
                start  =x[0]
                end = x[2]
                starts.append(start)
                ends.append(end)
                print start,end
        if line.find("</pre>") > -1:
            save = False

# looping over every file in the directory
for filename in os.listdir("pennregistrar/"):
    f = open("pennregistrar/"+filename, "r")
    parsefile(f)

# dividing up the classes we've found into different timeslots to count them
timeslots = defaultdict(int)
for i in range(len(starts)):
    timeslots[starts[i]+"-"+ends[i]] += 1

pprint(sorted(timeslots.items(), key=lambda x:x[1], reverse=True))
