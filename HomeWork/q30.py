inputList = []      # 輸入列表

# 重複讓使用者輸入直到停止(-1)
while True:
    tempInput = input()
    if(tempInput == '-1'):
        break
    inputList.append(tempInput)
# 遍歷輸入列表
for i in range(len(inputList)):
    # 初始答案為0
    ans = 0
    # 遍歷0~N並計算回饋次數
    for j in range(int(inputList[i], 2)+1):
        num = j
        while True:
            if(num <= 1):
                break
            elif(num % 2 == 0):
                ans += 1
                num = num/2
            else:
                ans += 1
                num = (num+1)/2
    print('{:014b}'.format(int(ans)))