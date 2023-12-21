def recursion(path, start, end, tempAns, finalAns) -> list:
    if(start == end):
        return [tempAns]
    for i in path:
        if(start in i):
            nextTribe = i[1-i.index(start)]
            if(nextTribe not in tempAns):
                ans = recursion(path, nextTribe, end, tempAns+[nextTribe], finalAns)
                for j in ans:
                    if(j not in finalAns):
                        finalAns.append(j)
    return finalAns         

pathNum, start, end = input().split()
breakPoint = list(map(int, input().split()))
path = list(list(map(int, input().split())) for _ in range(int(pathNum)))
tempAns = recursion(path, int(start), int(end), [int(start)], [])

if(len(tempAns) == 0): print("NO")
else:
    ans = []
    for i in breakPoint:
        for j in tempAns:
            if(i in j and j not in ans):
                ans.append(j)
        if(len(ans) == len(tempAns)): break
    ans = list(map(str, min(ans, key=lambda x:len(x))))
    for i in breakPoint:
        if(str(i) in ans):
            print(i, '\n', " ".join(ans), sep='')