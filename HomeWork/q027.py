amount_of_string = int(input())                         # 字串數量
depth = int(input())                                    # 深度
stringList = [input() for i in range(amount_of_string)] # 輸入字串
lBrackets = ['{', '[', '(']                             # 左括號
rBrackets = ['}', ']', ')']                             # 右括號
bracketsDic = {'{':'}', '[':']', '(':')'}               # 括號對應字典
for i in range(amount_of_string):
    stack = []                                          # 堆疊
    layer = 0                                           # 階層
    ans1 = 'pass'                                       # 答案1
    ans2 = ''                                           # 答案2
    # 依序判斷各自串
    for j in stringList[i]:
        # 如果當下層數等於要求深度且當前字符不等於括號則將此字符加入答案2中
        if(layer == depth and j not in (lBrackets + rBrackets)):
            ans2 += j
        # 如果當下字符屬於左括號則將它推入堆疊並將階層加一
        if(j in lBrackets):
            stack.append(j)
            layer += 1
        # 如果當下字符屬於又括號則嘗試判斷堆疊推出的字符是否與當前字符成對，若否則輸出fail
        elif(j in rBrackets):
            try:
                # 如果當前字符與堆疊出的字符成對則將階層減一，否則輸出fail
                if(bracketsDic[stack.pop()] == j):
                    layer -= 1
                else:
                    ans1 = 'fail'
                    break
            except:
                ans1 = 'fail'
                break
    # 如果堆疊長度不等於零代表有未必合的括號，輸出結果fail
    if(len(stack) != 0): 
        ans1 = 'fail'
    # 如果答案1等於fail，則直接印出fail為答案
    if(ans1 == 'fail'):
        print(ans1)
    # 如果答案1不等於fail，則判斷答案二是否為空並輸出對應答案
    else:
        if(ans2 == ''):
            print(ans1, 'EMPTY', sep=', ')
        else:
            print(ans1, ans2, sep=', ')