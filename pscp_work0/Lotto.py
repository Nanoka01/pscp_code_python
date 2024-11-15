"""Lotto"""
def calcuumoneywillgot():
    """Lotto"""
    Firstprize = input()
    Twolast = input()
    ThreeFront_one = input()
    ThreeFront_two = input()
    ThreeBack_one = input()
    ThreeBack_two = input()
    Youlotto = input()

    total =0
    Nearplus =""
    Neardown =""

    if Youlotto == Firstprize: #รางวัลที่1
        total = total + 6000000

    Check = Youlotto[4:6] #ท้าย2ตัว
    if Twolast == Check:
        total = total+ 2000

    Check = Youlotto[0:3]   #หน้า3ตัว
    if ThreeFront_one == Check: #หน้า3ตัว 1
        total = total + 4000
    if ThreeFront_two == Check: #หน้า3ตัว 2
        total = total + 4000

    Check = Youlotto[3:6]   #ท้าย 3 ตัว
    if ThreeBack_one == Check: #ท้าย 3 ตัว 1
        total = total + 4000
    if ThreeBack_two == Check: #ท้าย 3 ตัว 2
        total = total + 4000

    #เลขใกล้เคียง 1 (-)
    if Firstprize == "000000":
        Neardown = "999999"
    else:
        Neardown = str(int(Firstprize) - 1).zfill(6)
    if Youlotto == Neardown:
        total = total +100000

    #เลขใกล้เคียง 1 (+)
    if Firstprize == "999999":
        Nearplus = "000000"
    else:
        Nearplus = str(int(Firstprize) + 1).zfill(6)
    if Youlotto == Nearplus:
        total = total +100000

    print(total)
calcuumoneywillgot()
