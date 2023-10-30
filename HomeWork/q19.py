imageType = int(input())
lines = int(input())
if(imageType == 1):
    for i in range(1, lines+1):
        for j in range(1, 2*i//2+1): print(j, end='')
        for j in range(2*i//2-1, 0, -1): print(j, end='')
        print('')
elif(imageType == 2):
    for i in range(1, lines+1):
        print("_"*(lines-i), end='')
        for j in range(1, 2*i//2+1): print(j, end='')
        for j in range(2*i//2-1, 0, -1): print(j, end='')
        print("_"*(lines-i), end='')
        print('')
else:
    for i in range(lines, 0, -1):
        print("_"*(lines-i), end='')
        for j in range(1, 2*i//2+1): print(j, end='')
        for j in range(2*i//2-1, 0, -1): print(j, end='')
        print("_"*(lines-i), end='')
        print('')