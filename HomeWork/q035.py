schoolDic = {}
temp = [input().split() for _ in range(int(input()))]
for i in range(len(temp)):
    schoolDic[temp[i][0]] = temp[i][1::]

temp = [input().split(' + ') for _ in range(int(input()))]
searchType = int(input())

for i in range(len(temp)):
    for j in range(len(temp[i])):
        temp[i][j] = ("".join(temp[i][j])).split(' ')

if(searchType == 0):
    for i in range(len(temp)):
        tempAns = []
        for keys in schoolDic:
            for j in range(len(temp[i])):
                flag = True
                for t in temp[i][j]:
                    if(t not in schoolDic[keys]):
                        flag = False
                        break
                if(flag and keys not in tempAns):
                    tempAns.append(keys)
        print(*tempAns)
else:
    for i in range(len(temp)):
        temp[i] = [x for j in temp[i] for x in j]
    for i in range(len(temp)):
        tempDic = {}
        maximum = 0
        tempAns = []
        for keys in schoolDic:
            for j in temp[i]:
                if(j in schoolDic[keys]):
                    if(keys not in tempDic):
                        tempDic[keys] = 1
                    else:
                        tempDic[keys] += 1
        tempDic = dict(sorted(tempDic.items(), key=lambda x:x[1], reverse=True))
        for keys in tempDic:
            if(tempDic[keys] < maximum): break
            tempAns.append(keys)
            maximum = tempDic[keys]
        print(*tempAns)