myfile = open("pennregistrar/aamw.html")
for line in myfile:
    if (line.find("CU") != -1):
        print line
myfile.close()
