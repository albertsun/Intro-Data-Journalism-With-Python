# let's takle a look at some basic data structures, the list and the dictionary

# list
starts = ['3', '3:30', '2', '10:30', '1:30', '3', '4:30', '1:30', '3', '4:30']
ends = ['5PM', '6:30PM', '5PM', '12NOON', '3PM', '4:30PM', '6PM', '3PM', '4:30PM', '6PM']
print len(starts)
print starts[0]
print starts[:5]

# dictionary
d = {'5:30-7PM': 5, '8:30-5:30PM': 3, '9-1PM': 13, '7:30-10:30PM': 4, '5:30-6PM': 1, '6:30-8:30PM': 25, '9-4:30PM': 2, '7-10PM': 4, '5:30-7:30PM': 16, '7-7PM': 22}
print d['5:30-7PM']
d['5:30-7PM'] += 1
print d['5:30-7PM']

# the below line will cause an error if you uncomment it, because the dictionary doesn't have a key '6-9PM' in it
# d['6-9PM'] += 1


# we'll use a default dictionary instead, which has a default value
# that means we can add 1 to any key in it, even if it doesn't exist yet
# because the dictionary will take any unknown key and give it the default integer value of 0

# this is a different type of import statement
from collections import defaultdict

dd = defaultdict(int)
print dd
dd['6-9PM'] += 1
print dd
