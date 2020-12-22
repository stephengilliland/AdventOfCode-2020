depTime = 1000104
buses = [41,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',37,'x','x','x','x','x',659,'x','x','x','x','x','x','x',23,'x','x','x','x',13,'x','x','x','x','x',19,'x','x','x','x','x','x','x','x','x',29,'x',937,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',17]
orgBuses = [41,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',37,'x','x','x','x','x',659,'x','x','x','x','x','x','x',23,'x','x','x','x',13,'x','x','x','x','x',19,'x','x','x','x','x','x','x','x','x',29,'x',937,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',17]


busTimes = []
closest = 999999999
busIDs = []
ansBus = 0
currBus = 0
for x in range(len(buses)):
    if buses[x] != 'x':
        print(buses[x])
        busIDs.append(buses[x])
        while 1:
            buses[x] += orgBuses[x]
            print(buses[x])
            if buses[x] > depTime:
                break
        #print(buses[x])
        busTimes.append(buses[x])
for x in range(len(busTimes)):
    if busTimes[x] < closest and busTimes[x] > depTime:
        closest = busTimes[x]
        ansBus = busIDs[x]


print(busTimes)
print(closest)
print(depTime)
print(ansBus)
answer = (closest - depTime) * ansBus
print(answer)
