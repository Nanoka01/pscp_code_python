"""Shorten"""
def findshorten():
    """gunction"""
    run = 0
    ANS = ""
    alreadurun = False
    first = None
    before = None
    while True:
        try:
            num = int(input())
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if num == -1:
            break
        if not run:
            run = 1
            first = num
            before = num
        else:
            if before + 1 != num:
                if run == 2:
                    ANS = ANS + str(first) + "-" + str(before) + ", "
                    run = 1
                    first = num
                    before = num
                    alreadurun = True
                else:
                    ANS = ANS + str(before) + ", "
                    run = 1
                    before = num
                    alreadurun = True
            else:
                if alreadurun:
                    first = before
                    alreadurun = False
                before = num
                run = 2
    if run == 2:
        ANS = ANS + str(first) + "-" + str(before)
    elif run == 1:
        ANS = ANS + str(before)
    print(ANS)
findshorten()
