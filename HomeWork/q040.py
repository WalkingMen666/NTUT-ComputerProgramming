def primeNumber(num):
    for i in range(2, num):
        if(num%i==0):
            return False
    return True

startList = input()
endList = input().split()
inputList = input()
ans = []
index1 = 0
while True:
    if(startList in inputList[index1:]):
        index1 = inputList[index1:].find(startList)+index1
        for i in endList:
            tempIndex2 = len(inputList)
            while True:
                if(i in inputList[index1+len(startList):tempIndex2]):
                    tempIndex2 = inputList[index1+len(startList):tempIndex2].rfind(i)+index1+len(startList)
                    tempAns = inputList[index1+len(startList):tempIndex2]
                    
                    if(primeNumber(len(tempAns))):
                        check2 = True
                        for j in endList:
                            if(j in tempAns):
                                check2 = False
                                break
                        if(check2):
                            ans.append(tempAns)
                else:    
                    break
        index1 += len(startList)
    else: 
        break
    
if(len(ans) == 0): print('No gene')
else:
    ans = sorted(ans, key=lambda x:(len(x), x))
    for i in ans:
        print(i)