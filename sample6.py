# here we're going to use regular expressions to extract bits of text
# regular expressions are a sort of "sub" language that's used within other programming languages to match patterns
# the syntax looks a little obtuse at first, but they are an extremely powerful and useful tool
# here's a reference about them http://www.regular-expressions.info/


# to use regular expressions in Python, we have to import the regular expressions module, named re
# the import statement pulls in a bundle of functionality that we can access through the variable re
import re


# here's the content we'll look for things in
# go through and run this file three times.

one_class = """
AAMW-521  HSE/VILLA/PAL HELLEN ROM          1 CU
401 SEM W 3:30-6:30PM                 KUTTNER A
CROSS LISTED: ARTH-521 CLST-521
MAX W/CROSS LIST: 13
"""

# regular expression 1
def regex1(content):
    findtime = re.compile(r'(\d{1,2}:\d\d)')
    matches = findtime.findall(content)
    print matches

# regular expression 2, uncomment the lines below to run it
def regex2(content):
    findinstructor = re.compile(r'(\w+ [A-Z]\n)')
    matches = findinstructor.search(content)
    print matches.groups()

# regular expression 3, uncomment the lines below to run it
def regex3(content):
    findtimeranges = re.compile(r'(\d{1,2}(:\d\d)?)-((\d{1,2}(:\d\d)?)(([AP]M)|NOON))')
    matches = findtimeranges.search(content)
    print matches.groups()

regex1(one_class)
# regex2(one_class)
# regex3(one_class)
