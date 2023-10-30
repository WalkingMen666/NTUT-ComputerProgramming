def rounding(num:float):
    temp = num*1000//1
    if(temp % 10 > 5): temp += 10
    elif(temp % 10 == 5):
        if(temp // 10 % 10 % 2 == 1): temp += 10
    return temp//10/100
times = int(input())
bmiList = []
bmiDic = {}
tempAns, ans = 0, 0
for i in range(times):
    temp1, temp2 = input().split(' ')
    bmiList.append(rounding(float(temp2)/float(temp1)/float(temp1)))
bmiList.sort()
print(format(bmiList[times-1], '.2f'))
print(format(bmiList[0], '.2f'))
if(times % 2 == 1):
    print(format(bmiList[times//2], '.2f'))
else:
    print(format(rounding(((bmiList[times//2] + bmiList[times//2-1])/2)), '.2f'))
for i in range(times):
    if(not bmiList[i] in bmiDic):
        bmiDic[bmiList[i]] = 1
    else:
        bmiDic[bmiList[i]] += 1
for i in bmiDic:
    if(bmiDic[i] > tempAns): 
        ans = i
        tempAns = bmiDic[i]
print(format(ans,'.2f'))