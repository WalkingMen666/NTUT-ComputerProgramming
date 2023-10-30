height = float(input())
weight = float(input())

bmi = (weight/height/height)//0.001

if(bmi%10 < 5):
    bmi = bmi//10/100
elif(bmi % 10 > 5):
    bmi = (bmi + 10)//10/100
else:
    if(bmi//10%10%2 == 1):
        bmi = (bmi + 10)//10/100
    else:
        bmi = bmi//10/100
print('%.2f'%bmi)