playerScore, pcScore = 0, 0
playerGetCard, pcGetCard = True, True
cardList = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":0.5, "Q":0.5, "K":0.5}

while(playerGetCard or pcGetCard):
    num1, num2 = "", ""
    if(playerGetCard):
        num1 = input()
        playerScore += cardList[num1]
    if(playerScore > 10.5):
        playerScore = 0
        break
    if(pcGetCard):
        num2 = input()
        pcScore += cardList[num2]
    if(pcScore > 10.5):
        pcScore = 0
        break
    if(playerGetCard):
        temp = input()
        if(temp == "N"):
            playerGetCard = False
    if(pcScore >= playerScore and pcScore > 8):
        pcGetCard = False    

if(pcScore > playerScore): print("computer win")
elif(pcScore < playerScore): print("player win")
else: print("it's a tie")