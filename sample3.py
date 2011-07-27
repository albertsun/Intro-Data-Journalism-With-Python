myfile = open("pennregistrar/afrc.html")

count = 0
for line in myfile:

    # the find() method searches a string for the occurence of another string.
    # if it finds it, it returns the index where it occurs. if it's not found it returns -1
    if (line.find("CU") != -1):
        print line

        # this increments the value of count by 1
        count += 1

# cleaning up by closing the file we opened
myfile.close()
print count
