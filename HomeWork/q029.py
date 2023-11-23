inputList = []      # 輸入列表

# 重複讓使用者輸入直到停止(-1)
while True:
    inputList.append(input())
    if(input() == '-1'):
        break
# 遍歷輸入列表
for i in range(len(inputList)):
    # 紀錄回饋次數
    record = 0
    # 將輸入資料轉為十進制
    num = int(inputList[i], 2)
    # 重複計算回饋次數直到回饋資料為1
    while True:
        if(num <= 1):
            break
        elif(num % 2 == 0):
            record += 1
            num = num/2
        else:
            record += 1
            num = (num+1)/2
    # 將回饋次數轉為四位元二進制並印出
    print('{:04b}'.format(int(record)))