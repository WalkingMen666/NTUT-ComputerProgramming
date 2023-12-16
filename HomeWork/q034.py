def function1(friendShip, start, end, tempAns, finalAns, relationShip):
    if(start == end):
        tempAns.append(relationShip)
        return [tempAns]
    for keys in friendShip:
        if(keys[0] == start and keys[1] not in tempAns):
            ans = function1(friendShip, keys[1], end, tempAns+[keys[1]], finalAns, relationShip+min(int(friendShip[keys]), int(friendShip[keys[1]+keys[0]])))
            check = False
            for i in ans:
                if(i in finalAns):
                    check = True
                    break
            if(not check):
                finalAns += ans
    return finalAns
    
friendShip, _ = {}, input()
while True:
    temp = input().split(' ')
    if(len(temp) == 1):
        break
    friendShip[temp[0]+temp[1]] = temp[2]

ans = function1(friendShip, 'A', 'B', ['A'], [], 0)
print(len(min(ans, key=lambda x:len(x)))-2, "\n", " ".join(min(ans, key=lambda x:len(x))[:-1]), sep='')
print(max(ans, key=lambda x:x[-1])[-1], "\n", " ".join(max(ans, key=lambda x:len(x))[:-1]), sep='')