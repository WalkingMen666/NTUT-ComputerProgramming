strikeList, spareList = [False]*9, [False]*9
totalScore = []
ans = 0
for i in range(9):
    temp = int(input())
    totalScore.append(temp)
    if(temp == 10):
        totalScore.append(-1)
        strikeList[i] = True
    else:
        temp2 = int(input())
        totalScore.append(temp2)
        if(temp + temp2 == 10):
            spareList[i] = True       
score10_1 = int(input())
totalScore.append(score10_1)
if(score10_1 == 10):
    totalScore.append(int(input()))
    totalScore.append(int(input()))
else:
    score10_2 = int(input())
    totalScore.append(score10_2)
    if(score10_1 + score10_2 == 10):
        totalScore.append(int(input()))
for i in range(0, 18, 2):
    if(strikeList[i//2]):
        temp = 0
        for j in range(i+1, len(totalScore)):
            if(totalScore[j] != -1): 
                totalScore.append(totalScore[j])
                temp = j
                break
        for j in range(temp+1, len(totalScore)):
            if(totalScore[j] != -1):
                totalScore.append(totalScore[j])
                break
    elif(spareList[i//2]):
        for j in range(i+2, len(totalScore)):
            if(totalScore[j] != -1): 
                totalScore.append(totalScore[j])
                break

for i in totalScore:
    if(i != -1): ans += i
print(ans)