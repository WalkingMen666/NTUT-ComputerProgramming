stringA = input()           # 輸入字串A
stringB = input()           # 輸入字串B
vocX = input()              # 輸入單字X
vocY = input()              # 輸入單字Y

sentenceC = stringA + ' ' + stringB     # 將字串AB串聯成句子C
sentenceD = sentenceC.split(' ')        # 將句子C變成list，方便之後替換
sentenceE = sentenceD.copy()            # 複製句子C為句子D
sentenceF = sentenceC[0]                # 將句子F初始化為句子C的第一個字母
gap = abs(len(vocX)-len(vocY))          # 計算單字X跟單字Y的字數差異

# 依序替換句子C中的單字X為單字Y及句子E的單字X為逆者的單字Y
for i in range(len(sentenceD)):
    if(sentenceD[i].lower() == vocX.lower()):
        sentenceD[i] = vocY
        sentenceE[i] = vocY[::-1]

# 將句子D(list)變成字串
ansD = " ".join(sentenceD)
# 將句子E(list)變成字串
ansE = " ".join(sentenceE)

# 依序新增句子C中的指定字符到句子F中，若遇連續空格則跳過
for i in range(gap, len(sentenceC), gap):
    if(sentenceC[i] != ' ' or (sentenceC[i] == ' ' and sentenceF[-1] != ' ')):
        sentenceF += sentenceC[i]

# 計算句子C不包含空格的長度
cLength = sum([len(i) for i in sentenceC.split()])
# 計算句子D不包含空格的長度
dLength = sum([len(i) for i in sentenceD])

# 輸出各答案
print(sentenceC)
print(ansD)
print(cLength, dLength)
print(ansE)
print(sentenceF)