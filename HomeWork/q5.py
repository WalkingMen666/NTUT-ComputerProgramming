def getTriangle(a, b, c):
    if((((a+b+c) - max(a, b, c)) <= max(a, b,c)) or a <=0 or b <= 0 or c <= 0):
        print("not a triangle")
    elif(a==b and b==c):
        print("equilateral triangle")
    elif(a==b and a**2+b**2 > c**2):
        print("isosceles triangle")
    elif(b==c and b**2+c**2 > a**2):
        print("isosceles triangle")
    elif(a==c and a**2+c**2 > b**2):
        print("isosceles triangle")
    else:
        biggest = max(a, b, c)
        smallest = min(a, b, c)
        mid = (a + b + c) - biggest - smallest
        if(biggest**2 > (mid**2 + smallest**2)):
            print("obtuse triangle")
        elif(biggest**2 < (mid**2 + smallest**2)):
            print("acute triangle")
        else:
            print("right triangle")

a = int(input())
b = int(input())
c = int(input())

getTriangle(a, b, c)