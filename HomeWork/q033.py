# 使用者輸入座標並儲存成列表形式放到posList中
posList = list(list(map(int, input().split()))for _ in range(int(input())))
# 答案
ans = []

# 計算無人機間的距離並將兩台的編號及距離放到答案列表中
for i in range(len(posList)):
    for j in range(i+1, len(posList)):
        pos1 = posList[i][1::]
        pos2 = posList[j][1::]
        dis = ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2+(pos1[2]-pos2[2])**2)**0.5
        ans.append([posList[i][0]] + [posList[j][0]] + [dis])
print(ans)
# 針對答案列表的第二項(距離)做排序
ans = sorted(ans, key = lambda x:x[2])

# 印出答案->依據答案列表中的前兩項(無人機編號)對應到posList並印出無人機座標
for i in range(3):
    print(ans[i][0], ans[i][1], *posList[ans[i][0]-1][1::], *posList[ans[i][1]-1][1::])