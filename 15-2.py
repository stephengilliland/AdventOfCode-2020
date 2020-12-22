spoken = [9,6,0,10,18,2,1]
lastSpoken = spoken[len(spoken)-1]
seen = { 9: 0, 6: 1, 0: 2, 10: 3, 18: 4, 2: 5 }
while len(spoken) != 30000000:
    if lastSpoken not in seen:
        nextSpoken = 0
    elif lastSpoken in seen:
        nextSpoken = len(spoken) - seen[lastSpoken] - 1
    seen[lastSpoken] = len(spoken)-1
    spoken.append(lastSpoken)
    lastSpoken = nextSpoken
print(lastSpoken) 