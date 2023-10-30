def eqTriangle(n:int):
    for i in range(n):
        for _ in range(n-1-i): print("#", end='')
        for _ in range((i+1)*2-1): print("*", end='')
        for _ in range(n-1-i): print("#", end='')
        print('')
def inTriangle(n:int):
    for i in range(n-1, -1, -1):
        for _ in range(n-i-1): print("#", end='')
        for _ in range((i+1)*2-1): print("*", end='')
        for _ in range(n-i-1): print("#", end='')
        print('')
def diamond(n:int):
    for i in range(n):
        if(i < n//2):
            for _ in range((n//2+1)-(((i+1)*2-1)//2+1)): print(' ', end='')
            for _ in range((i+1)*2-1): print("*", end='')
        elif(i == n//2):
            for _ in range(n): print("*", end='')
        else:
            for _ in range((n//2+1)-(((n-i)*2-1)//2+1)): print(' ', end='')
            for _ in range((n-i)*2-1): print("*", end='')
        print('')
def fish(n:int):
    for i in range(n):
        if(i < n//2):
            for _ in range((n//2+1)-(((i+1)*2-1)//2+1)): print(' ', end='')
            for _ in range((i+1)*2-1): print("*", end='')
            for _ in range((n//2+1)-(((i+1)*2-1)//2+1)): print(' ', end='')
            for _ in range(n//2-(((i+1)*2-1)//2)): print(' ', end='')
            for _ in range(((i+1)*2-1)//2): print("-", end='')
        elif(i == n//2):
            for _ in range(n): print("*", end='')
            for _ in range(n//2): print('-', end='')
        else:
            for _ in range((n//2+1)-(((n-i)*2-1)//2+1)): print(' ', end='')
            for _ in range((n-i)*2-1): print("*", end='')
            for _ in range((n//2+1)-(((n-i)*2-1)//2+1)): print(' ', end='')
            for _ in range(n//2-(((n-i)*2-1)//2)): print(' ', end='')
            for _ in range(((n-i)*2-1)//2): print("-", end='')
        print('')
    
imageType = int(input())
lines = int(input())
if(lines % 2 == 1 and lines >= 3 and lines <= 49):
    if(imageType == 1):
        eqTriangle(lines)
    elif(imageType == 2):
        inTriangle(lines)
    elif(imageType == 3):
        diamond(lines)
    else:
        fish(lines)
else:
    print("error")