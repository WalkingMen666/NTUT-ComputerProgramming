population = int(input())       # n 城市人口
days = int(input())             # m 計算期間
confirmedCase = int(input())    # a 確診人數
infect = float(input())         # b 傳染人數
recoverDays = int(input())      # c 康復天數
immunityRate = float(input())   # d 免疫率

new_confirmed_case_list = [confirmedCase]   # 紀錄新增的確診人數
remain_Recover_Days = [recoverDays]         # 紀錄剩餘的康復天數

# 先印出第一天的情況
print(1, confirmedCase, confirmedCase, 0)

for i in range(2, days+1):
    # 初始化今天的確診人數
    new_to_confirmed_case = 0
    
    # 將康復天數-1
    for j in range(len(remain_Recover_Days)):
        remain_Recover_Days[j] -= 1
    
    # 計算今天的康復人數
    recoverPopulation = sum([new_confirmed_case_list[j] for j in range(len(remain_Recover_Days)) if(remain_Recover_Days[j] == 0)])
    
    # 計算前一天的總確診人數
    last_total_confirmed_case = sum([new_confirmed_case_list[j] for j in range(len(remain_Recover_Days)) if remain_Recover_Days[j] > -1])
    
    # 如果總確診人數小於可以確診的人數則計算新增的確診人數
    if(not (sum(new_confirmed_case_list) >= int(population*(1-immunityRate)))):
        # 計算今天新增的確診人數
        new_to_confirmed_case = int(last_total_confirmed_case*(infect/recoverDays)*(1-immunityRate))
        
        # 計算今天的總確診人數
        confirmed_case_until_now = sum([new_confirmed_case_list[j] for j in range(len(remain_Recover_Days)) if remain_Recover_Days[j] > 0]) + new_to_confirmed_case
        
        # 如果今天確診的人數大於可以確診的人數則將今天的確診人數改至最大值
        if(confirmed_case_until_now > int(population*(1-immunityRate))):
            new_to_confirmed_case = new_to_confirmed_case - (confirmed_case_until_now-int(population*(1-immunityRate)))
        
        # 如果今天新增的確診人數大於0則將它加入確診紀錄列表並新增一康復天數參數至康復紀錄列表
        if(new_to_confirmed_case > 0):
            remain_Recover_Days.append(recoverDays)
            new_confirmed_case_list.append(new_to_confirmed_case)
    
    # 計算今天的總確診人數
    confirmed_case_until_now = sum([new_confirmed_case_list[j] for j in range(len(remain_Recover_Days)) if remain_Recover_Days[j] > 0])
    
    # 如果天數大於康復天數則開始計算免疫率
    if(i > recoverDays):
        immunityRate = immunityRate + recoverPopulation/population
    
    # 印出當天情況
    print(i, confirmed_case_until_now, new_to_confirmed_case, recoverPopulation)

# 印出累計天數的總確診人數    
print(sum(new_confirmed_case_list))