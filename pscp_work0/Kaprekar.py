"""Kaprekar"""
x = input()
total = 0
ANS = x
zero = "0"
while True:
    hight =""
    lower =""
    word = ANS
    if ANS == "6174": 
        break
    curretnum = x[0]
    for i in range(4):
        curretnum = word[0]
        for j in range(1, len(word)):
            nextnum = word[j]
            if int(nextnum) > int(curretnum):
                curretnum = nextnum
        word = word.replace(curretnum,"",1)
        hight = hight + curretnum
    word = ANS
    curretnum = word[0]
    for i in range(4):
        curretnum = word[0]
        for j in range(1, len(word)):
            nextnum = word[j]
            if int(nextnum) < int(curretnum):
                curretnum = nextnum
        word = word.replace(curretnum,"",1)
        lower = lower + curretnum
    ANS = int(hight) - int(lower)
    ANS = str(ANS)
    if len(ANS) <= 3:
        ANS = ANS + zero
    total = total+1
print(total)
