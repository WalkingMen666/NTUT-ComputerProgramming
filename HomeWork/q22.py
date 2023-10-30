def check(cardList:list):
    tempLength = 0
    tempList, cardDicList = [], []
    for i in cardList:
        cardDic = {"A":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "J":0, "Q":0, "K":0}
        suitsDic = {"S":0, "H":0, "D":0, "C":0}
        if(len(i) != 5): return 1, ""
        for j in i:
            if(j[0:-1:] not in cardDic): return 1, ""
            else: cardDic[j[0:-1:]] += 1
            if(j[-1::] not in suitsDic): return 1, ""
            else: suitsDic[j[-1::]] += 1
            tempList.append(j)
        if(len(i) != len(set(i))): return 2, ""
        tempLength += len(i)
        cardDicList.append([cardDic, suitsDic])
    if(tempLength != len(set(tempList))): return 2, ""
    else: return 3, cardDicList

counts = int(input())
tempInput = [input().split(' ') for i in range(counts)]
nameList, cardList, ansList = [], [], []
error = 3

for i in range(counts):
    nameList.append(tempInput[i][0])
    cardList.append(tempInput[i][1::])
error, cardDicList = check(cardList)

if(error != 3):
    if(error == 1): print("Error input")
    else: print("Duplicate deal")
else:
    for i in range(counts):
        numList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3', '4']
        cardType, pair, three_of_a_kind = 1, 0, 0
        cont = [False]*len(numList)
        flush = False
        
        for key in cardDicList[i][0]:
            if(cardDicList[i][0][key] == 2):
                cardType = max(2, cardType)
                pair += 1
            elif(cardDicList[i][0][key] == 3):
                cardType = max(4, cardType)
                three_of_a_kind += 1
            elif(cardDicList[i][0][key] == 4): cardType = 8
        if(pair == 2): cardType = max(3, cardType)
        if(three_of_a_kind > 0 and pair > 0): cardType = max(7, cardType)
        
        for key in cardDicList[i][1]:
            if(cardDicList[i][1][key] == 5):
                cardType = max(6, cardType)
                flush = True
        
        tempList = list(cardDicList[i][0].keys())
        for j in range(len(numList)):
            if(cardDicList[i][0][numList[j]] > 0):
                cont[j] = True
        for j in range(13):
            if(cont[j]):
                try:
                    if(cont[j] and cont[j+1] and cont[j+2] and cont[j+3] and cont[j+4]):
                        if(flush): cardType = 9
                        else: cardType = max(5, cardType)
                except:
                    break
        ansList.append(cardType)
    
    for i in range(counts):
        for j in range(i+1, counts):
            if(ansList[j] > ansList[i]):
                ansList[i], ansList[j] = ansList[j], ansList[i]
                nameList[i], nameList[j] = nameList[j], nameList[i]
    for i in range(counts):
        print(nameList[i], ansList[i])