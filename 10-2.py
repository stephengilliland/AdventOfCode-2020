adpt = [0 , 1 , 2 , 3 , 4 , 7 , 8 , 9 , 10 , 13 , 16 , 17 , 18 , 19 , 22 , 23 , 24 , 25 , 26 , 29 , 30 , 31 , 32 , 33 , 36 , 37 , 38 , 41 , 42 , 43 , 44 , 47 , 50 , 51 , 52 , 53 , 56 , 57 , 58 , 61 , 64 , 65 , 66 , 69 , 70 , 71 , 72 , 75 , 76 , 77 , 80 , 81 , 82 , 83 , 84 , 87 , 88 , 89 , 90 , 93 , 96 , 97 , 98 , 99 , 100 , 103 , 104 , 105 , 108 , 111 , 114 , 115 , 118 , 121 , 122 , 123 , 124 , 127 , 128 , 129 , 130 , 131 , 134 , 137 , 138 , 139 , 140 , 143 , 146 , 149 , 150 , 151 , 152 , 155 , 156 , 157 , 160 , 161 , 164 , 165 , 166 , 167 , 168 , 171 , 172 , 173 , 174 , 177 , 180 , 181 , 182 , 183 , 184 , 184 , 184]
onesCtr = 1
threesCtr = 1
x = 0
answer = 1
ansCtr = 0
adpt.sort()
answersList = []
ones = []
threes = []

while x <= len(adpt)-2:
    onesCtr = 1
    threesCtr = 1

    while adpt[x+1] == adpt[x] + 1 and x <= len(adpt)-1:
        onesCtr += 1
        x += 1
    if onesCtr:
        ones.append(onesCtr)
    while adpt[x+1] == adpt[x] + 3 and x <= len(adpt)-1:
        threesCtr += 1
        x += 1
    if threesCtr:
        threes.append(threesCtr)
    if x >= len(adpt) - 3:
        break

for x in range(len(ones)):
    #print(ones[x])
    if ones[x] == 2:
        answer *= 1   
    if ones[x] == 3:
        answer *= 2 
    if ones[x] == 4:
        answer *= 4 
    if ones[x] == 5:
        answer *= 7 
print("Answer =",answer)

