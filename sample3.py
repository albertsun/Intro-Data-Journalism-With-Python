myfile = open("pennregistrar/afrc.html")

count = 0
for line in myfile:

    # the find() method searches a string for the occurence of another string.
    # if it finds it, it returns the index where it occurs. if it's not found it returns -1
    if (line.find("CU") != -1):
        print line
        count += 1

myfile.close()
print count
