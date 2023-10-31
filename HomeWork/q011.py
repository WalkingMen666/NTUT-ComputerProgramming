import math
bookInfo = input().split(','), input().split(','), input().split(',')
price = [380, 1200, 180]
newBookInfo, priceArray = [], []
sum = 0

for i in range(3):
    temp = [int(bookInfo[i][0]), int(bookInfo[i][1]), int(bookInfo[i][2]), int(bookInfo[i][3])]
    newBookInfo.append(temp)

for i in range(3):
    if(int(newBookInfo[i][0]) <= 10): priceArray.append(int(price[i]*newBookInfo[i][0]))
    elif(int(newBookInfo[i][0]) <= 20): priceArray.append(int(math.ceil(price[i]*newBookInfo[i][0]*newBookInfo[i][1]/100)))
    elif(int(newBookInfo[i][0]) <= 30): priceArray.append(int(math.ceil(price[i]*newBookInfo[i][0]*newBookInfo[i][2]/100)))
    elif(int(newBookInfo[i][0]) > 30): priceArray.append(int(math.ceil(price[i]*newBookInfo[i][0]*newBookInfo[i][3]/100)))

finalPrice = {priceArray[0]:"A", priceArray[1]:"B", priceArray[2]:"C"}
priceArray.sort()
print(finalPrice[priceArray[2]],",", priceArray[2], sep='')
print(finalPrice[priceArray[1]],",", priceArray[1], sep='')
print(finalPrice[priceArray[0]],",", priceArray[0], sep='')
print(priceArray[0]+priceArray[1]+priceArray[2])