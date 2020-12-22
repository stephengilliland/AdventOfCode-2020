spoken = [9,6,0,10,18,2,1]
lastSpoken = spoken[len(spoken)-1]
while len(spoken) != 2020:
    if spoken.count(lastSpoken) == 1:
        nextSpoken = 0
    else:
        for x in range(len(spoken)-2, -1, -1):
            if spoken[x] == lastSpoken:
                nextSpoken = len(spoken) - 1 - x
                break
    spoken.append(nextSpoken)
    lastSpoken = nextSpoken
print(lastSpoken)