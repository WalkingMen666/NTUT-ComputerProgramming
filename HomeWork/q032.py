# 使用者輸入初始矩陣
inputMatrix = [list(map(int, input().split())) for _ in range(4)]

# 不斷執行判斷直到沒有0
while True:
    # 判斷還有沒有0
    temp = inputMatrix[0]+inputMatrix[1]+inputMatrix[2]+inputMatrix[3]
    if(0 not in temp):
        break
    # 計算直欄
    for i in range(4):
        column = [inputMatrix[x][i] for x in range(4)]
        # 如果直欄有0且只有一個0，則將0更改為正解
        if(0 in column and len(set(column)) == 4):
            inputMatrix[column.index(0)][i] = 10 - sum(column)
    # 計算橫列
    for i in range(4):
        row = inputMatrix[i]
        # 如果橫列有0且只有一個0，則將0更改為正解
        if(0 in row and len(set(row)) == 4):
            inputMatrix[i][row.index(0)] = 10 - sum(row)
    # 分別計算各區域
    # 取得區塊的值
    for i in range(0, 4, 2):
       for j in range(0, 4, 2):
           block = [inputMatrix[i][j]]+[inputMatrix[i][j+1]]+[inputMatrix[i+1][j]]+[inputMatrix[i+1][j+1]]
           if(0 in block and len(set(block)) == 4):
               inputMatrix[i+block.index(0)//2][j+block.index(0)%2]=10-sum(block)
# 印出矩陣
for i in range(4):
    print(*inputMatrix[i])