# 格雷碼計算
def grayCode(n, k):
    if(n == 1):
        # 直接回傳字串型態的k
        return str(k)
    elif(k < 2**(n-1)):
        # 回傳 '0' + 下一次的格雷碼回傳值
        return '0' + grayCode(n-1, k)
    else:
        # 回傳 '1' + 下一次的格雷碼回傳值
        return '1' + grayCode(n-1, 2**(n)-1-k)
    
inputList = []      # 輸入列表

# 重複讓使用者輸入直到停止(-1)
while True:
    temp = input()
    if(temp == '-1'):
        break
    else:
        # 將使用者的輸入分開並利用map函式統一為int接者再轉換成列表
        inputList.append(list(map(int, temp.split())))

# 遍歷輸入列表
for i in range(len(inputList)):
    # 呼叫格雷碼函示並印出回傳值(答案)
    print(grayCode(inputList[i][0], inputList[i][1]))