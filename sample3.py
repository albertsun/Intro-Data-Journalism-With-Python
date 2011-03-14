myfile = open("pennregistrar/afrc.html")

count = 0
for line in myfile:
    if (line.find("CU") != -1):
        print line
        count += 1
myfile.close()
print count
