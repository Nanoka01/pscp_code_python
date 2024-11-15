"""Diginity"""
while True:
    x = input()
    if x == "0":
        break
    Roundrun = len(x)
    if Roundrun >1:
        FRISTNUM = x[0]
        for i in range (Roundrun-1):
            secondnum = x[1+i]
            FRISTNUM = int(FRISTNUM) + int(secondnum)
            FRISTNUM = str(FRISTNUM)
            ROUNDINLOOPCHECK = len(FRISTNUM)
            if ROUNDINLOOPCHECK > 1:
                secondnum = FRISTNUM[1]
                FRISTNUM = FRISTNUM[0]
                FRISTNUM = int(FRISTNUM) + int(secondnum)
        print(FRISTNUM)
    else:
        FRISTNUM = x[0]
        print(FRISTNUM)
