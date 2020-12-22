import copy
from itertools import combinations
slices = [
"##..####",
".###....",
"#.###.##",
"#....#..",
"...#..#.",
"#.#...##",
"..#.#.#.",
".##...#."]

#slices = [
#".#.",
#"..#",
####",
#]

ctr = 0
options = [0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1]
combins = combinations(options, 4)
combos = set(combins)
fourD = [[[['.' for i in range(25)] for z in range(25)] for y in range(25)] for x in range(25)]

for i in range(10, 11):
        for z in range(10, 11):
            for y in range(10, 10+len(slices)):
                for x in range(10, 10+len(slices[0])):
                    fourD[i][z][y][x] = slices[10-y][10-x]
                                                        ##
fourD[10][10][10] = ['.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
fourD[10][10][11] = ['.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
fourD[10][10][12] = ['.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
fourD[10][10][13] = ['.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
fourD[10][10][14] = ['.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
fourD[10][10][15] = ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
fourD[10][10][16] = ['.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '#', '#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
fourD[10][10][17] = ['.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
#['#', '.', '#', '#', '.', '#', '.', '.']
#['#', '#', '.', '.', '.', '.', '.', '#']
#['.', '#', '#', '.', '.', '#', '#', '#']
##['.', '#', '#', '.', '#', '.', '.', '.']
#['#', '.', '#', '.', '.', '.', '#', '.']
#['#', '.', '.', '#', '.', '.', '.', '.']
#['#', '.', '#', '.', '#', '#', '#', '#']
#['#', '.', '#', '.', '.', '#', '.', '.']
#print(fourD)
for i in range(1, 19):
        for z in range(1, 19):
            for y in range(1, 19):
                if '#' in fourD[i][z][y]:
                    print(i, z, y)
                    print(fourD[i][z][y])

testCtr = 0
for d in range(6):
    fourDNew = copy.deepcopy(fourD)
    print("")
    print("")
    for i in range(1, 24):
        for z in range(1, 24):
            for y in range(1, 24):
                if '#' in fourD[i][z][y]:
                    #print(i, z, y)
                    for x in range(len(fourD[i][z][y])):
                        print(fourD[i][z][y][x], end='')
                    print('')
                for x in range(1, 24):
                    ctr = 0
                    for combo in combos:
                        combo = list(combo)
                        if combo != [0,0,0,0]:
                            if fourD[i+combo[0]][z+combo[1]][y+combo[2]][x+combo[3]] == '#':
                                ctr += 1
                    if fourD[i][z][y][x] == '#':
                        if ctr == 2 or ctr == 3:
                            fourDNew[i][z][y][x] = '#'
                        else:
                            fourDNew[i][z][y][x] = '.'

                    elif fourD[i][z][y][x] == '.':
                        if ctr == 3:
                            fourDNew[i][z][y][x] = '#'
                        else:
                            fourDNew[i][z][y][x] = '.'

    fourD = copy.deepcopy(fourDNew)
    """
    for i in range(25):
        for z in range(25):
            for y in range(25):
                if '#' in fourD[i][z][y]:
                    #print(i, z, y)
                    for x in range(len(fourD[i][z][y])):
                        print(fourD[i][z][y][x], end='')
                    print('')
    """
ctr = 0
for i in range(25):
        for z in range(25):
            for y in range(25):
                for x in range(25):
                    #print(fourD[i][z][y][x])
                    if fourD[i][z][y][x] == '#':
                        ctr += 1
print(ctr)