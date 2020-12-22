busesWGaps = [41,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',37,'x','x','x','x','x',659,'x','x','x','x','x','x','x',23,'x','x','x','x',13,'x','x','x','x','x',19,'x','x','x','x','x','x','x','x','x',29,'x',937,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',17]
buses = [41,37,659,23,13,19,29,937,17]
orgBuses = [41,37,659,23,13,19,29,937,17]
# Gaps     [0, 34, 39,46,50,55,64, 65,81]
busGaps = []
gapCtr = 0
ctr = 0
number = 99999999999544
number = 205549400000000
orgNumber = 293642
done = False
#busesWGaps = [7,13,'x','x',59,'x',31,19]
#buses = [7,13,59,31,19]
#number = 6   234103497000000
#             103529892120000
#             000000000000000
#BWG        [41, 2,618,-26,-41,-41,-41,865,-72]
#orgBuses = [41,37,659, 23, 13, 19, 29,937,17]



#for x in range(len(busesWGaps)):
#    if busesWGaps[x] != 'x':
#        busGaps.append(gapCtr)
#    gapCtr += 1
#print(busGaps)

for x in range(len(buses)):
    buses[x] -= busGaps[x]
print(buses)

while 1:
    number += orgNumber  
    if not pow(number, 1, 29364200000):
        print("Time",number)
    if pow((number), 1, 1874) == 0:
        if pow((number), 1, 1318) == 0:
                 if pow((number), 1, 74) == 0:
                         if pow((number), 1, 46) == 0:
                                if pow((number), 1, 34) == 0:
                                        done = True




    #    for x in range(len(buses)):
    #        if pow((number + busGaps[x]), 1, buses[x]):
    #            #print("BAD")
    #            done = False
    if done == True:
        print(number)
        break
    
    # 168659158
    #110000000000000 too Low
    #150000000000000 too low
    #200000000000000 too low 





