numList = [int(input()) for i in range(6)]
ans = 0
for i in range(0, 6, 2):
    ans += numList[i+1]-numList[i]
    
for i in range(0, 4, 2):
    for j in range(i+2, 6, 2):
        if(numList[i+1] > numList[j]):
            if(numList[j+1] < numList[i+1]): ans -= abs(numList[j]-numList[j+1])
            else: ans -= abs(numList[i+1]-numList[j])
print(ans)