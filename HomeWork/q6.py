import math

a = int(input())
b = int(input())
c = int(input())

tempAns = b**2-4*a*c

if(tempAns >= 0):
    print("%.1f"%((-b+math.sqrt(tempAns))/2/a))
    print("%.1f"%((-b-math.sqrt(tempAns))/2/a))
else:
    print("%.1f"%(-b/2/a), "+%.1fi"%(math.sqrt(tempAns*-1)/2/a), sep='')
    print("%.1f"%(-b/2/a), "-%.1fi"%(math.sqrt(tempAns*-1)/2/a), sep='')