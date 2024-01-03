import math

def rank(target, headCount, pre = 0, ans = 0):
    for i in range(1, 101):
        ans = math.ceil(headCount*i/100)-pre
        pre += ans
        if(pre == target): return i
    
courseList, subject_year_ans, course_year_ans, searchList = [], [], [], []
subject_year_dic, course_year_dic, searchDic, searchAns = {}, {}, {}, {}

for i in range(int(input())):
    temp = input().split()
    stu = []
    for j in range(int(temp[-1])):
        stu.append(input().split())
    courseList.append([temp,stu])
search = input()

# courseList = [[[課程編碼, 學期編號, 學生數][[學號, 學期成績, (會考成績)], [...], ...]], 
#               [[課程編碼, 學期編號, 學生數][[學號, 學期成績, (會考成績)], [...], ...]]]

# subject_year_dic = {"科系+年級+學年":{"學號":[[學期成績, (會考成績), 學分數], ...], "學號":[[學期成績, (會考成績), 學分數], ...]},
#                     "科系+年級+學年":{"學號":[[學期成績, (會考成績), 學分數], ...], "學號":[[學期成績, (會考成績), 學分數], ...]}}

# course_year_dic = {"課程+學年":[[學號, 學期成績, (會考成績)], [...], ...],
#                    "課程+學年":[[學號, 學期成績, (會考成績)], [...], ...]}

# 整理資料
for i in range(len(courseList)):
    if(courseList[i][0][0] == search):
        searchList += courseList[i][-1]
    for j in range(len(courseList[i][1])):
        subjectInfo = courseList[i][1][j][0][3:6]+courseList[i][1][j][0][:3]+courseList[i][0][1][:-1]
        courseInfo = courseList[i][0][0]+courseList[i][0][1][:-1]
        
        if(subjectInfo not in subject_year_dic):
            subject_year_dic[subjectInfo] = {courseList[i][1][j][0]:[courseList[i][1][j][1:]+[courseList[i][0][0][-1]]]}
        else:
            if(courseList[i][1][j][0] not in subject_year_dic[subjectInfo]):
                subject_year_dic[subjectInfo].update({courseList[i][1][j][0]:[courseList[i][1][j][1:]+[courseList[i][0][0][-1]]]})
            else:
                subject_year_dic[subjectInfo][courseList[i][1][j][0]] += [courseList[i][1][j][1:]+[courseList[i][0][0][-1]]]

        if(courseInfo not in course_year_dic): course_year_dic[courseInfo] = [courseList[i][1][j]]
        else: course_year_dic[courseInfo] += [courseList[i][1][j]]

# 問題一 【subject_year_ans】
for key1 in subject_year_dic:
    temp = [[key1, len(subject_year_dic[key1])]]
    for key2 in subject_year_dic[key1]:
        score, count, unSubscribe = 0, 0, 0
        for i in subject_year_dic[key1][key2]:
            if(len(i) == 3):
                score += int(math.ceil(int(i[0])*0.7+int(i[1])*0.3)*int(i[-1]))
                count += int(i[-1])
            elif(i[0] == 'w'):
                unSubscribe += 1
            else:
                score += int(i[0])*int(i[-1])
                count += int(i[-1])
        if(unSubscribe == len(subject_year_dic[key1][key2])):
            temp.append([key2, 0, 0, 100])
        else:
            temp.append([key2, int(score/(count)), 0, int(unSubscribe/len(subject_year_dic[key1][key2])*100)])
    temp = [temp[0]] + sorted(sorted(temp[1:], key=lambda x:x[0], reverse=False), key=lambda x:x[1], reverse=True)
    subject_year_ans.append(temp)
subject_year_ans = sorted(subject_year_ans, key=lambda x:x[0])
for i in range(len(subject_year_ans)):
    for j in range(1, len(subject_year_ans[i])):
        subject_year_ans[i][j][2] = rank(j, subject_year_ans[i][0][-1])
for i in range(len(subject_year_ans)):
    print(subject_year_ans[i][0][0][:3], subject_year_ans[i][0][0][3:6], subject_year_ans[i][0][0][6:])
    for j in range(1, 4):
        print("{0[0]} {0[1]} {0[2]}% {0[3]}%".format(subject_year_ans[i][j]))

# 問題二 【course_year_ans】
for keys in course_year_dic:
    temp = [[keys, 0, 0, 0, 0, len(course_year_dic[keys])]]
    unSubscribe, score = 0, 0
    for i in course_year_dic[keys]:
        if(len(i) == 3):
            temp.append([i[0], int(math.ceil(int(i[1])*0.7+int(i[2])*0.3)), 0])
            score += int(math.ceil(int(i[1])*0.7+int(i[2])*0.3))
        elif(i[1] == 'w'):
            unSubscribe += 1
        else:
            temp.append([i[0], int(i[1]), 0])
            score += int(i[1])
    temp[0][1] = str(max(temp[1:], key=lambda x:x[1])[1])
    temp[0][2] = str(int(score/(len(course_year_dic[keys])-unSubscribe)))
    temp[0][3] = str(min(temp[1:], key=lambda x:x[1])[1])
    temp[0][4] = str(int(unSubscribe/len(course_year_dic[keys])*100))
    temp = [temp[0]] + sorted(sorted(temp[1:], key=lambda x:int(x[0]), reverse=False), key=lambda x:x[1], reverse=True)
    course_year_ans.append(temp)
    
course_year_ans = sorted(course_year_ans, key=lambda x:x[0][0])
for i in range(len(course_year_ans)):
    for j in range(1, len(course_year_ans[i])):
        course_year_ans[i][j][2] = rank(j, course_year_ans[i][0][-1])
for i in range(len(course_year_ans)):
    print(course_year_ans[i][0][0][:4], course_year_ans[i][0][0][4:])
    print("{0[0]} {0[1]} {0[2]} {0[3]}%".format(course_year_ans[i][0][1:-1]))
    for j in range(1, 4):
        print("{0[0]} {0[1]} {0[2]}%".format(course_year_ans[i][j]))

# 問題三
for i in range(len(searchList)):
    if(len(searchList[i]) == 3):
        if(searchList[i][0] not in searchAns):
            searchAns[searchList[i][0]] = int(math.ceil(int(searchList[i][1])*0.7+int(searchList[i][2])*0.3))
        else:
            searchAns[searchList[i][0]] = max(searchAns[searchList[i][0]], int(math.ceil(int(searchList[i][1])*0.7+int(searchList[i][2])*0.3)))
    elif(searchList[i][1] == 'w'):
        pass
    else:
        if(searchList[i][0] not in searchAns):
            searchAns[searchList[i][0]] = int(searchList[i][1])
        else:
            searchAns[searchList[i][0]] = max(searchAns[searchList[i][0]], int(searchList[i][1]))
    if(searchList[i][0][3:6] not in searchDic):
        searchDic[searchList[i][0][3:6]] = 1
    else:
        searchDic[searchList[i][0][3:6]] += 1    

searchAns = sorted(sorted(searchAns.items(), key=lambda x:int(x[0]), reverse=False), key=lambda x:x[1], reverse=True)
searchDic = sorted(sorted(searchDic.items(), key=lambda x:int(x[0]), reverse=False), key=lambda x:x[1], reverse=True)
tempCount = 0
for i in range(2):
    print(searchAns[i][0], end=' ')

for i in searchDic:
    print(i[0], end=' ')
    tempCount += 1
    if(tempCount == 2):
        break