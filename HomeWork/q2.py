import math

a = int(input())
b = int(input())
c = int(input())

print(round((((-b) + math.sqrt(b*b-4*a*c)) / (2*a)), 1))
print(round((((-b) - math.sqrt(b*b-4*a*c)) / (2*a)), 1))