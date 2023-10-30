cardList = input().split(' ')
numList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4']
suits = ['S', 'H', 'D', 'C']
cont = [False]*len(numList)
error, cardType, pair, three_of_a_kind = 0, 1, 0, 0
cardDic, suitsDic = {}, {}
flush = False

if(len(cardList) != 5): error = 1
elif(len(cardList) != len(set(cardList))): error = 2
for c in cardList:
    if(len(c) > 3 or len(c) <= 1): error = 1
    elif(len(c) == 3):
        if((c[0]+c[1]) not in numList or c[2] not in suits): error = 1
        else: 
            if((c[0]+c[1]) not in cardDic): cardDic[c[0]+c[1]] = 1
            else: cardDic[c[0]+c[1]] += 1
            if(c[2] not in suitsDic): suitsDic[c[2]] = 1
            else: suitsDic[c[2]] += 1
    elif(c[0] not in numList or c[1] not in suits): error = 1
    else:
        if(c[0] not in cardDic): cardDic[c[0]] = 1
        else: cardDic[c[0]] += 1
        if(c[1] not in suitsDic): suitsDic[c[1]] = 1
        else: suitsDic[c[1]] += 1

if(error == 0):
    for key in cardDic:
        if(cardDic[key] == 2):
            cardType = max(2, cardType)
            pair += 1
        elif(cardDic[key] == 3): 
            cardType = max(4, cardType)
            three_of_a_kind += 1
        elif(cardDic[key] == 4): cardType = 8
    if(pair == 2): cardType = max(3, cardType)
    if(three_of_a_kind > 0 and pair > 0): cardType = max(7, cardType)
    
    if(len(suitsDic) == 1):
        cardType = max(6, cardType)
        flush = True
    
    tempList = list(cardDic.keys())
    for i in range(len(numList)):
        if(numList[i] in tempList):
            cont[i] = True
    
    for i in range(13):
        if(cont[i]):
            try:
                if(cont[i] and cont[i+1] and cont[i+2] and cont[i+3] and cont[i+4]):
                    if(flush): cardType = 9    
                    else: cardType = max(5, cardType)
            except:
                break
    print(cardType)
else:
    if(error == 1): print("Error input")
    else: print("Duplicate deal")