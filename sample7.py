"""
A data cleaning question from NICAR-L
"""


old = """Smith, John
12345 A Street
Colorado Springs CO
County: El Paso
Reason for submission: To go on vacation
Miller, Rebecca
45678 A Street
Colorado Springs CO
County: El Paso
Reason for submission: To take a break"""

new = """
Smith, John                        12345 A Street                   Colorado Springs CO                       County: El Paso                 Reason for submission: To go on vacation
Miller, Rebecca                 45678 A Street                   Colorado Springs CO                       County: El Paso                 Reason for submission: To take a break
"""


lines = old.split("\n")
for i in xrange(0,len(lines),5): print('\t'.join([x.strip() for x in lines[i:i+5]])+'\n')


"""
# To run on files

with open("old.txt") as old:
    with open("new.txt","w") as new:
        lines = old.readlines()
        for i in xrange(0,len(lines),5): new.write('\t'.join([x.strip() for x in lines[i:i+5]])+'\n')
"""
