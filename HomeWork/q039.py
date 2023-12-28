n, _ = int(input()), input()
tempA, tempB = list(map(int, input().split())), list(map(int, input().split()))
select = list(map(int, input().split()))

matrixA, matrixB = [], []
scoreA, scoreB = 0, 0

for i in range(0, len(tempA), n):
    matrixA.append(tempA[i:i+n])
    matrixB.append(tempB[i:i+n])

for i in range(n):
    checkA, checkB = True, True
    for x, y in zip(matrixA[i], matrixB[i]):
        if(x not in select):
            checkA = False
        if(y not in select):
            checkB = False
    if(checkA): scoreA += 1
    if(checkB): scoreB += 1
    
    checkA, checkB = True, True
    tempA, tempB = [], []
    for j in range(n):
        tempA.append(matrixA[j][i])
        tempB.append(matrixB[j][i])
    for x, y in zip(tempA, tempB):
        if(x not in select):
            checkA = False
        if(y not in select):
            checkB = False
    
    if(checkA): scoreA += 1
    if(checkB): scoreB += 1

checkA, checkB = True, True
for i in range(n):
    if(matrixA[i][i] not in select):
        checkA = False
    if(matrixB[i][i] not in select):
        checkB = False            
if(checkA): scoreA += 1
if(checkB): scoreB += 1

checkA, checkB = True, True
for i in range(n):
    temp = n-i-1
    if(matrixA[i][temp] not in select):
        checkA = False
    if(matrixB[i][temp] not in select):
        checkB = False            
if(checkA): scoreA += 1
if(checkB): scoreB += 1

if(scoreA > scoreB): print("A Win")
elif(scoreA < scoreB): print("B Win")
else: print("Tie")