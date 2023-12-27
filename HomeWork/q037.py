courseList = []
for i in range(int(input())):
    temp = input().split()
    stu = []
    for j in range(int(temp[-1])):
        stu.append(input().split())
    courseList.append([temp,stu])
search = input()

# ('學號', ''):['學號', '課程+年分+三位元成績']