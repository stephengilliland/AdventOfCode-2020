oneCards = [28, 13, 25, 16, 38, 3, 14, 6, 29, 2, 47, 20, 35, 43, 30, 39, 21, 42, 50, 48, 23, 11, 34, 24, 41]
twoCards = [27, 37, 9, 10, 17, 31, 19, 33, 40, 12, 32, 1, 18, 36, 49, 46, 26, 4, 45, 8, 15, 5, 44, 22, 7]
answer = 0

while oneCards and twoCards:
    oneCard = oneCards.pop(0)
    twoCard = twoCards.pop(0)
    if oneCard > twoCard:
        oneCards.append(oneCard)
        oneCards.append(twoCard)
    elif twoCard > oneCard:
        twoCards.append(twoCard)
        twoCards.append(oneCard)
if oneCards:    
    for x in range(len(oneCards)-1, -1, -1):
        answer = answer + (len(oneCards) - x) * oneCards[x]
if twoCards:
    for x in range(len(twoCards)-1, -1, -1):
        answer = answer + (len(twoCards) - x) * twoCards[x]
print(answer)