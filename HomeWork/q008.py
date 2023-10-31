def check(class_Info:list, checkList:list):    
    string:str = class_Info[0][len(class_Info[0])-4:]
    if((not class_Info[1].isnumeric()) or int(class_Info[1]) <= 0 or int(class_Info[1]) > 3): return True
    if(not string.isnumeric()): return True
    for i in range(2,len(class_Info)):
        if((not class_Info[i][0].isnumeric()) or int(class_Info[i][0]) < 1 or int(class_Info[i][0]) > 5): return True
        elif not(class_Info[i][1] in checkList): return True
    return False
def main():
    class_1_Info = [input() for i in range(2)]
    for i in range(int(class_1_Info[1])): class_1_Info.append(input())
    class_2_Info = [input() for i in range(2)]
    for i in range(int(class_2_Info[1])): class_2_Info.append(input())
    class_3_Info = [input() for i in range(2)]
    for i in range(int(class_3_Info[1])): class_3_Info.append(input())
    checkList = ['1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c']
    unExpected = check(class_1_Info, checkList) or check(class_2_Info, checkList) or check(class_3_Info, checkList)
    if(unExpected): print("-1")
    else:
        wrong = False
        for i in range(2, len(class_2_Info)): 
            if(class_2_Info[i] in class_1_Info): 
                print(class_1_Info[0], ",", class_2_Info[0], ",", class_2_Info[i], sep='')
                wrong = True
        for i in range(2, len(class_3_Info)): 
            if(class_3_Info[i] in class_1_Info): 
                print(class_1_Info[0], ",", class_3_Info[0], ",", class_3_Info[i], sep='')
                wrong = True
        for i in range(2, len(class_3_Info)): 
            if(class_3_Info[i] in class_2_Info): 
                print(class_2_Info[0], ",", class_3_Info[0], ",", class_3_Info[i], sep='')
                wrong = True
        if(not wrong): print("correct")
main()