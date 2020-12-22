import copy
slices = [[
"##..####",
".###....",
"#.###.##",
"#....#..",
"...#..#.",
"#.#...##",
"..#.#.#.",
".##...#."]]
empty = [
"........",
"........",
"........",
"........",
"........",
"........",
"........",
"........"
]
"""
slices = [[
".#.",
"..#",
"###",
]]
empty = [
"...",
"...",
"..."
]
"""
nextSlices = []
turns = 6
ctr = 0

for x in range(len(empty)):
    slices[0][x] = list(slices[0][x])
    empty[x] = list(empty[x])

def countAdj(downLayer, layer, upLayer, yPos, xPos):
    hashCtr = 0
    if layer[yPos+1][xPos+1] == '#':# M - top right
        hashCtr += 1
    if layer[yPos+1][xPos] == '#':# M - Top
        hashCtr += 1
    if layer[yPos][xPos+1] == '#':# M - Right
        hashCtr += 1
    if layer[yPos-1][xPos-1] == '#':# M - Mottom Left
        hashCtr += 1
    if layer[yPos-1][xPos] == '#':# M - Mottom
        hashCtr += 1
    if layer[yPos][xPos-1] == '#':# M Left
        hashCtr += 1
    if layer[yPos+1][xPos-1] == '#':# M - Top Left
        hashCtr += 1
    if layer[yPos-1][xPos+1] == '#':# M - Mottom Righy
        hashCtr += 1

    # Below 
    if downLayer[yPos+1][xPos+1] == '#':# B - top right
        hashCtr += 1
    if downLayer[yPos+1][xPos] == '#':# B - Top
        hashCtr += 1
    if downLayer[yPos][xPos+1] == '#':# B - Right
        hashCtr += 1
    if downLayer[yPos-1][xPos-1] == '#':# B - Bottom Left
        hashCtr += 1
    if downLayer[yPos-1][xPos] == '#':# B - Bottom
        hashCtr += 1
    if downLayer[yPos][xPos-1] == '#':# B Left
        hashCtr += 1
    if downLayer[yPos+1][xPos-1] == '#':# B - Top Left
        hashCtr += 1
    if downLayer[yPos-1][xPos+1] == '#':# B - Bottom Righy
        hashCtr += 1
    if downLayer[yPos][xPos] == '#': # B Middle
        hashCtr += 1

    # Above
    if upLayer[yPos+1][xPos+1] == '#':# B - top right
        hashCtr += 1
    if upLayer[yPos+1][xPos] == '#':# B - Top
        hashCtr += 1
    if upLayer[yPos][xPos+1] == '#':# B - Right
        hashCtr += 1
    if upLayer[yPos-1][xPos-1] == '#':# B - Bottom Left
        hashCtr += 1
    if upLayer[yPos-1][xPos] == '#':# B - Bottom
        hashCtr += 1
    if upLayer[yPos][xPos-1] == '#':# B Left
        hashCtr += 1
    if upLayer[yPos+1][xPos-1] == '#':# B - Top Left
        hashCtr += 1
    if upLayer[yPos-1][xPos+1] == '#':# B - Bottom Righy
        hashCtr += 1
    if upLayer[yPos][xPos] == '#':
        hashCtr += 1

    return hashCtr

emptyRow = []

for z in range(6):

    for x in range(len(empty)):
        empty[x].insert(0, '.')
        empty[x].append('.')
    emptyRow = []
    for x in range(len(empty[0])):
        emptyRow.append('.')
    empty.insert(0, copy.deepcopy(emptyRow))
    empty.append(copy.deepcopy(emptyRow))
    empty.insert(0, copy.deepcopy(emptyRow))
    empty.append(copy.deepcopy(emptyRow))

    for y in range(len(slices)):
        for x in range(len(slices[y])):
            slices[y][x].insert(0, '.')
            slices[y][x].append('.')
    print("ALL SLICES")
    for slic in slices:
        slic.append(copy.deepcopy(empty[0]))
        slic.insert(0, copy.deepcopy(empty[0]))
        slic.append(copy.deepcopy(empty[0]))
        slic.insert(0, copy.deepcopy(empty[0]))
    print(len(slices))

    slices.insert(0, copy.deepcopy(empty))
    slices.append(copy.deepcopy(empty))
    slices.insert(0, copy.deepcopy(empty))
    slices.append(copy.deepcopy(empty))

    for slic in slices:
        for row in slic:
            print(row)
        print("")

    nextSlices = copy.deepcopy(slices)

    for l in range(1, len(slices)-1):

        currLayer = slices[l]
        prevLayer = slices[l-1]
        nextLayer = slices[l+1]

        for y in range(1, len(slices[l])-1):
            #print("Y", y)
            for x in range(1, len(slices[l][y])-1):
                #print("x", x)
                ctr = countAdj(prevLayer, currLayer, nextLayer, y, x)
                print(x,y,'=', ctr)
                if currLayer[y][x] == '#':
                    if ctr == 2 or ctr == 3:
                        nextSlices[l][y][x] = '#'
                    else:
                        nextSlices[l][y][x] = '.'
                elif currLayer[y][x] == '.':
                    if ctr == 3:
                        nextSlices[l][y][x] = '#'
                    else:
                        nextSlices[l][y][x] = '.'
    slices = copy.deepcopy(nextSlices)

answer = 0
for z in range(len(slices)):
    for y in range(len(slices[z])):
        for x in range(len(slices[z][y])):
            if slices[z][y][x] == '#':
                answer += 1
print(answer)


