def check(class_Info:list, checkList:list):    
    string:str = class_Info[0][len(class_Info[0])-4:]
    if((not class_Info[1].isnumeric()) or int(class_Info[1]) <= 0 or int(class_Info[1]) > 3): return True
    if(not string.isnumeric()): return True
    for i in range(2,len(class_Info)):
        if((not class_Info[i][0].isnumeric()) or int(class_Info[i][0]) < 1 or int(class_Info[i][0]) > 5): return True
        elif not(class_Info[i][1] in checkList): return True
    return False
classInfo = []
checkList = ['1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c']
excepted = False
for _ in range(int(input())):
    temp = []
    temp.append(input())
    temp.append(input())
    for i in range(int(temp[1])):
        temp.append(input())
    classInfo.append(temp)
for i in range(len(classInfo)):
    excepted = excepted or check(classInfo[i], checkList)
if(excepted):
    print("-1")
else:
    wrong = False
    for i in range(len(classInfo)-1):
        for t in range(i+1, len(classInfo)):
            for j in range(2, len(classInfo[i])):
                if(classInfo[i][j] in classInfo[t]):
                    print(classInfo[i][0], ",", classInfo[t][0], ",", classInfo[i][j], sep = '')
                    wrong = True
    if(not wrong):
        print("correct")