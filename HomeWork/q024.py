cardList = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":0.5, "Q":0.5, "K":0.5}
playerNums = int(input())
betList = list(map(lambda x: int(x), input().split(' ')))
tempScore = list(map(lambda x: cardList[x], input().split(' ')))
playerScore = [float(x) for x in tempScore[1::]]
pcScore, pcBet, minScore = tempScore[0], 0, 11
playerExplode, pcGetCard = [False]*playerNums, True

# Player get card
for i in range(playerNums):
    while(True):    
        tempList = input().split(' ')
        if(len(tempList) != 1):
            playerScore[i] += cardList[tempList[1]]
        else:
            break
        if(playerScore[i] == 10.5):
            break
        elif(playerScore[i] > 10.5):
            playerExplode[i] = True
            break

# Calculate min score
for i in range(playerNums):
    if(playerScore[i] < minScore and playerScore[i] <= 10.5):
        minScore = playerScore[i]
        
# Check if pc need to get card
for i in playerExplode:
    pcGetCard = pcGetCard and i
if(not pcGetCard):
    if(playerScore.count(10.5) == playerNums):
        pcGetCard = False
    else:
        pcGetCard = True
else:
    pcGetCard = False
    
# Computer get card
while(pcGetCard):
    if(pcScore > 10.5):
        pcScore = 0
        pcGetCard = False
        break
    elif(pcScore == 10.5 or pcScore > minScore):
        pcGetCard = False
        break
    pcScore += cardList[input()]

# Judge
for i in range(playerNums):
    if(playerScore[i] == 10.5):
        pcBet -= betList[i]
        print("Player", i+1, " +", betList[i], sep='')
    elif(playerExplode[i] or playerScore[i] <= pcScore):
        pcBet += betList[i]
        print("Player", i+1, " -", betList[i], sep='')
    elif((not playerExplode[i]) and playerScore[i] > pcScore):
        pcBet -= betList[i]
        print("Player", i+1, " +", betList[i], sep='')
if(pcBet > 0): print("Computer +", pcBet, sep='')
else: print("Computer", pcBet)