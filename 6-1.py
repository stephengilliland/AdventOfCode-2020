file = open('6-1.txt', 'r') 
currGroup = ""
groups = []
uniq = []
ctr = 0

while 1: 
    char = file.read(1)          
    if not char:  
        break
    if char == ',':
        groups.append(currGroup)
        print("Group: ",currGroup)
        currGroup = ""
    else:
        currGroup += char

for group in groups:
    print(group)
    for x in range(len(group)):
        if group[x] not in uniq and group[x] != "\n":
            #print(group[x])
            uniq.append(group[x])
    ctr += len(uniq)
    print(len(uniq))
    uniq = []

print(ctr)
#a5019
#16244
#14994
#6589