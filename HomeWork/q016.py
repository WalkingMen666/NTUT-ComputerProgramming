def getTriangelInfo(tInfo: list):
    tInfo.sort()
    temp = sum(tInfo)/2
    area = (temp*(temp-tInfo[0])*(temp-tInfo[1])*(temp-tInfo[2]))**0.5
    if((tInfo[0]+tInfo[1]) <= tInfo[2] or tInfo[0] <= 0 or tInfo[1] <= 0 or tInfo[2] <= 0): return "not a triangle", "WRONG"
    elif(tInfo[0] == tInfo[1] and tInfo[1] == tInfo[2] and tInfo[0] == tInfo[2]): return "equilateral triangle", area
    elif(tInfo[0] == tInfo[1] or tInfo[0] == tInfo[2] or tInfo[1] == tInfo[2]): return "isosceles triangle", area
    elif((tInfo[2]**2) > (tInfo[0]**2+tInfo[1]**2)): return "obtuse triangle", area
    elif((tInfo[2]**2) < (tInfo[0]**2+tInfo[1]**2)): return "acute triangle", area
    elif((tInfo[2]**2) == (tInfo[0]**2+tInfo[1]**2)): return "right triangle", area
    
times = int(input())
inputList, areaList = [], []
for _ in range(times):
    inputList.append([int(i) for i in input().split(' ')])
for i in range(times):
    ans, area = getTriangelInfo(inputList[i])
    if(area != "WRONG"):
        areaList.append(round(area, 2))
        print(ans, "%.2f" %area)
    else:
        print(ans)
if(len(areaList) == 0): 
    print("All inputs are not triangles!")
else:
    print("%.2f" %max(areaList))
    print("%.2f" %min(areaList))