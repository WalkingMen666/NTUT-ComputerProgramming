# Check if the input cardSet is not allowed
def check(cardList:list):
    numList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['S', 'H', 'D', 'C']
    for i in cardList:
        if(i[0] not in suits): return 1
        elif(i[1::] not in numList): return 1
    if(len(cardList) != len(set(cardList))): return 2
    return 3

# Get which card type this cardSet is
def getCardType(card:list):
    cardList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4']
    numList, suitsList = [], []
    cardType, pair, three_of_a_kind = 1, 0, 0
    cont = [False]*len(cardList)
    flush = False
    numDic, suitsDic = {}, {}
    for i in card:
        suitsList.append(i[0])
        numList.append(i[1::])
    
    for i in range(len(card)):
        if(suitsList[i] not in suitsDic):
            suitsDic[suitsList[i]] = 1
        else:
            suitsDic[suitsList[i]] += 1
        if(numList[i] not in numDic):
            numDic[numList[i]] = 1
        else:
            numDic[numList[i]] += 1
    
    for key in numDic:
        if(numDic[key] == 2):
            cardType = max(2, cardType)
            pair += 1
        elif(numDic[key] == 3):
            cardType = max(4, cardType)
            three_of_a_kind += 1
        elif(numDic[key] == 4):
            cardType = max(8, cardType)
    if(pair == 2):
        cardType = max(3, cardType)
    elif(pair > 0 and three_of_a_kind > 0):
        cardType = max(7, cardType)
    
    for key in suitsDic:
        if(suitsDic[key] == 5):
            cardType = max(6, cardType)
            flush = True
    
    tempList = list(numDic.keys())
    for i in range(len(cardList)):
        if(cardList[i] in tempList):
            cont[i] = True
    for i in range(13):
        if(cont[i]):
            try:
                if(cont[i] and cont[i+1] and cont[i+2] and cont[i+3] and cont[i+4]):
                    if(flush): cardType = 9
                    else: cardType = max(5, cardType)
            except:
                break
    return cardType

# Find the biggest cardType from all the possible cardSet
def getBestSet(cardList:list):
    score = 0
    for i in range(6):
        score = max(score, getCardType(cardList[i:i+6:]))
    return score

# Input then Check
playerCard = [input().split(' ') for _ in range(2)]
cardList = input().split(' ')
checkList = playerCard[0] + playerCard[1] + cardList
error = check(checkList)

# Print the Ans
if(error == 1): print("Error input")
elif(error == 2): print("Duplicate deal")
else:
    playerAScore = getBestSet(cardList+playerCard[0]+cardList)
    playerBScore = getBestSet(cardList+playerCard[1]+cardList)
    if(playerAScore > playerBScore): 
        print("A", playerAScore)
    elif(playerAScore < playerBScore): 
        print("B", playerBScore)
    else:
        print("Tie")