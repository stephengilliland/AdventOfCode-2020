oneCards = [28, 13, 25, 16, 38, 3, 14, 6, 29, 2, 47, 20, 35, 43, 30, 39, 21, 42, 50, 48, 23, 11, 34, 24, 41]
twoCards = [27, 37, 9, 10, 17, 31, 19, 33, 40, 12, 32, 1, 18, 36, 49, 46, 26, 4, 45, 8, 15, 5, 44, 22, 7]
answer = 0
states = []
gameOver = False

def subGame(p1Cards, p2Cards):
    subStates = []
    winner = 0
    while p1Cards and p2Cards:
        subState = (p1Cards+[':']+p2Cards)
        if subState in subStates:
            break
        else:
            subStates.append(subState)

        p1Card = p1Cards.pop(0)
        p2Card = p2Cards.pop(0)

        if p1Card <= len(p1Cards) and p2Card <= len(p2Cards):
            winner = subGame(p1Cards[:p1Card], p2Cards[:p2Card])

        if winner == 1:
            p1Cards.append(p1Card)
            p1Cards.append(p2Card)
        elif winner == 2:
            p2Cards.append(p2Card)
            p2Cards.append(p1Card)
        elif p1Card > p2Card or winner == 1:
            p1Cards.append(p1Card)
            p1Cards.append(p2Card)
        elif p2Card > p1Card or winner == 2:
            p2Cards.append(p2Card)
            p2Cards.append(p1Card)
        winner = 0
        
    if p1Cards:
        return 1
    elif p2Cards:
        return 2


winr = 0
while oneCards and twoCards:

    state = (oneCards+[':']+twoCards)
    if state in states:
        print("REPEATED STATE")
        break
    else:
        states.append(state)

    oneCard = oneCards.pop(0)
    twoCard = twoCards.pop(0)

    if oneCard <= len(oneCards) and twoCard <= len(twoCards):
        winr = subGame(oneCards[:oneCard], twoCards[:twoCard])
        if gameOver:
            break
    if winr == 1:
        oneCards.append(oneCard)
        oneCards.append(twoCard)
    elif winr == 2:
        twoCards.append(twoCard)
        twoCards.append(oneCard)
    elif oneCard > twoCard:
        oneCards.append(oneCard)
        oneCards.append(twoCard)
    elif twoCard > oneCard:
        twoCards.append(twoCard)
        twoCards.append(oneCard)
    winr = 0

if oneCards:    
    for x in range(len(oneCards)-1, -1, -1):
        answer = answer + (len(oneCards) - x) * oneCards[x]

if twoCards:
    for x in range(len(twoCards)-1, -1, -1):
        answer = answer + (len(twoCards) - x) * twoCards[x]

print("Answer =",answer)