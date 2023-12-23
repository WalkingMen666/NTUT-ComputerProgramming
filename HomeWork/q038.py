def recursion(caveList, start, end, gold, tempAns, finalAns) -> list:
    if(start == end):
        return [tempAns[:-1]+[gold]]
    for i in caveList:
        if(i[0] == start):
            for j in i[2:]:
                if(j not in tempAns):
                    ans = recursion(caveList, j, end, gold+i[1], tempAns+[j], finalAns)
                else:
                    ans = [tempAns+[gold+i[1]]]
                for t in ans:
                    if(t not in finalAns):
                        finalAns.append(t)
    return finalAns

nums, start = input().split()
caveList = list(list(map(int, input().split())) for _ in range(int(nums)))
gold = 0

for i in caveList:
    if(i[0] == int(start)): gold = i[1]

ans = recursion(caveList, int(start), 0, 0, [int(start)], [])
print(max(ans, key=lambda x:x[-1])[-1])