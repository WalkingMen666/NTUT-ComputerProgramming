def turnLeft(matrix:list):
    ans = []
    for i in range(len(matrix)-1, -1, -1):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        ans.append(temp)
    return ans

def turnRight(matrix:list):
    ans = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix)-1, -1, -1):
            temp.append(matrix[j][i])
        ans.append(temp)
    return ans

matrixList = []
lines = int(input())
for i in range(lines):
    matrixList.append([int(x) for x in range(lines*i+1, lines*i+1+lines)])
action = input()
for i in action:
    if(i == "L"): matrixList = turnLeft(matrixList)
    else: matrixList = turnRight(matrixList)
for i in range(lines):
    for j in range(lines):
        print(matrixList[i][j], end=' ')
    print('')