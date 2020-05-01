import re

g = open("downloadlist.txt", "r")
for line in g:
    substring = re.search("edgar/data/(.*?).txt", line).group(1)
    substring = substring.replace('-','')
    print("edgar/data/" + substring)
g.close()
