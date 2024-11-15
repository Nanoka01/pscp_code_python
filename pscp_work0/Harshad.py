"""Harshad"""
for i in range(10):
    i = i*1
    DIVISIONHARSHAD = 0
    NUM = int(input())
    if NUM :
        NUM = abs(NUM)
        NUM = str(NUM)
        for char in NUM:
            DIVISIONHARSHAD = int(DIVISIONHARSHAD) + int(char)
        NUM = int(NUM)
        if not NUM % DIVISIONHARSHAD:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
        