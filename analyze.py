#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, re

findhours = re.compile(r'(\d{1,2}(:\d\d)?)-(\d{1,2}(:\d\d)?(([AP]M)|NOON))')
starts = []
ends = []

def parsefile(f):
    save = False
    for line in f:
        if line.find("<pre>") > -1:
            save = True
            lines = []
        if (save == True):
            m = findhours.search(line)
            if m:
                x = m.groups()
                start  =x[0]
                end = x[2]
                starts.append(start)
                ends.append(end)
                print start,end
            #lines.append(line)
        if line.find("</pre>") > -1:
            save = False
            #return lines

for filename in os.listdir("pennregistrar/"):
    f = open("pennregistrar/"+filename, "r")
    #f = open("pennregistrar/aamw.html", "r")
    parsefile(f)
