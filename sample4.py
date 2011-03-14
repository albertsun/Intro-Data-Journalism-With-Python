import re

content = """
AAMW-521  HSE/VILLA/PAL HELLEN ROM          1 CU
 401 SEM W 3:30-6:30PM                 KUTTNER A
     CROSS LISTED: ARTH-521 CLST-521
     MAX W/CROSS LIST: 13"""

findtime = re.compile(r'(\d{1,2}:\d\d)')
matches = findtime.search(content)
print matches.groups()

# findinstructor = re.compile(r'([A-Z]+ [A-Z]\n)')
# matches = findinstructor.search(content)
# print matches.groups()


# findtimeranges = re.compile(r'(\d{1,2}(:\d\d)?)-((\d{1,2}(:\d\d)?)(([AP]M)|NOON))')
# matches = findtimeranges.search(content)
# print matches.groups()
