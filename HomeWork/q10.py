downArray = [False, False]
score = [int(input())]
totalScore = 0

if(not score[0] == 10):
    score.append(int(input()))
    if(sum(score) == 10): 
        downArray[1] = True
else: 
    downArray[0] = True
score.append(int(input()))
if(not score[len(score)-1] == 10):
    score.append(int(input()))
    if(score[len(score)-2] + score[len(score)-1] == 10): 
        score.append(int(input()))
else:
    score.append(int(input()))
    score.append(int(input()))
totalScore = sum(score)
if(downArray[0]):
    totalScore += (score[1] + score[2])
elif(downArray[1]):
    totalScore += score[2]
print(totalScore)