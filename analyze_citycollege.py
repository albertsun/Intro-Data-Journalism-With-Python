#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import re
from collections import defaultdict


find_cuny_hours = re.compile(r'(\d{1,2}(:\d\d)?)\s*-\s*((\d{1,2}(:\d\d)?)\s*(([AP]M)|NOON))')

if __name__ == "__main__":

   soup = BeautifulSoup(open("citycollege/registrar.html"))
   
   starts = []
   ends = []

   coursetables = soup.findAll("table", {"class":"coursetable"})
   for course in coursetables:
       classtimes = course.findAll("td", text=re.compile(r'\d{1,2}:\d\d'))
       for c in classtimes:
           m = find_cuny_hours.search(c)
           if m:
               x = m.groups()
               start = x[0]
               end = x[2]
               starts.append(start)
               ends.append(end)
               print start,end
           else:
               print "No match found"
               print c
   print "found %(count)d total class times" % { "count": len(starts) }
   
   # dividing up the classes we've found into different timeslots to count them
   timeslots = defaultdict(int)
   for i in range(len(starts)):
       timeslots[starts[i]+"-"+ends[i]] += 1

   print(sorted(timeslots.items(), key=lambda x:x[1], reverse=True)[:10])
