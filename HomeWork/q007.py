inCall = int(input())
outCall = int(input())
cityCall = int(input())
inMsg = int(input())
outMsg = int(input())
internet = int(input())

price1 = inCall*0.08+outCall*0.139+cityCall*0.135+inMsg*1.128+outMsg*1.483
price2 = inCall*0.07+outCall*0.13+cityCall*0.121+inMsg*1.128+outMsg*1.483
price3 = inCall*0.06+outCall*0.108+cityCall*0.101+inMsg*1.128+outMsg*1.483
price4 = max(inCall*0.05+outCall*0.1+cityCall*0.09+inMsg*1.128+outMsg*1.483, 1283)

if(internet-1 > 0): price1 = max((price1 + 250*(internet-1)), 183)
else: price1 = max(price1, 183)
if(internet-3 > 0): price2 = max((price2 + 200*(internet-3)), 383)
else: price2 = max(price2, 383)
if(internet-5 > 0): price3 = max((price3 + 150*(internet-5)), 983)
else: price3 = max(price3, 983)

cheaptest = int(min(price1, price2, price3, price4))
print(cheaptest)

if(cheaptest < 383): print("183")
elif(cheaptest < 983): print("383")
elif(cheaptest < 1283): print("983")
else: print("1283")