#!/usr/bin/python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup

def parse(filename):
    soup = BeautifulSoup(open(filename))

    

if __name__ == "__main__":
   #parse("citycollege/registrar.html")
   if not soup:
       soup = BeautifulSoup(open("citycollege/registrar.html"))
   else:
       print "soup already parsed"
   
   # print soup.find("font", "orange")
   print len(soup.findAll("font", {"class": "orange"})) #counts number of occurences of font tag with class "orange"
