busesWGaps = [41,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',37,'x','x','x','x','x',659,'x','x','x','x','x','x','x',23,'x','x','x','x',13,'x','x','x','x','x',19,'x','x','x','x','x','x','x','x','x',29,'x',937,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',17]

buses = [41,37,659,23,13,19,29,937,17]
orgBuses = [41,37,659,23,13,19,29,937,17]
# Gaps     [0, 34, 39,46,50,55,64, 65,81]
busGaps = []
gapCtr = 0
ctr = 0
number = 0
orgNumber = 41
done = False
secMatch = False
firstMatch = False
"""
buses = [7,13,59,31,19]
orgBuses = [7,13,59,31,19]
busesWGaps = [7,13,'x','x',59,'x',31,19]
"""
matches = 0
matchCtr = 0
lowNum = 0
highNumber = 0
for x in range(len(busesWGaps)):
    if busesWGaps[x] != 'x':
        busGaps.append(gapCtr)
    gapCtr += 1
print(busGaps)
print(buses)

#for x in range(len(buses)):
#    buses[x] -= busGaps[x]
#print(buses)


while 1:
    number += orgNumber
    if not pow(number, 1, 100000):
        print(orgNumber)
        print("Time =",number)
    if matches == 3:
        print(number)
        print(buses[matches])
        
    if ((number + busGaps[matches]) % buses[matches] == 0) or matches == 0:
        print("True")
        if not firstMatch:
            firstMatch = True
            lowNum = number
        else:
            secMatch = True
            highNum = number

        if firstMatch and matches == len(buses)-1:
            print("did a bad thing")
            secMatch = False
            firstMatch = False
            if matchCtr > matches: 
                matches = matchCtr 
            if matchCtr == len(buses)-1:
                print("Answer =",number)
                quit() 

        if secMatch:
            print("Low =", lowNum)
            print("High =",highNum)
            matchCtr += 1
            secMatch = False
            firstMatch = False
            if matchCtr > matches: 
                #print(buses[matches])
                matches = matchCtr 
                number = lowNum
                orgNumber = highNum - lowNum
                print("Start Time:", number)
                print("Time Jump:", orgNumber)
                print("Diff:",orgNumber)
                print(buses[matches])
                print("")
            if matchCtr == len(buses):
                print(number)
                quit()
    else:
        secMatch = False






