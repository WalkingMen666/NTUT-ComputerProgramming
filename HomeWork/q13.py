times = int(input())
recordList = [0]*40
ans = 0
for i in range(times):
    temp1, temp2 = input().split(' ')
    for j in range(int(temp1)+20, int(temp2)+20):
        recordList[j] += 1
for i in range(times):
    for j in range(40):
        if(recordList[j] > 1):
            recordList[j] -= 1         
print(sum(recordList))