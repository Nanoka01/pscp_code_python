"""Loto"""
def main():
    """main"""
    pr1 = input()
    back2 = input()
    font3_1 = input()
    font3_2 = input()
    back3_1 = input()
    back3_2 = input()
    me = input()
    near1 = ""
    near2 = ""
    money = 0
    if pr1 == "000000":
        near1 = "000001"
        near2 = "999999"
    elif pr1 == "999999":
        near1 = "000000"
        near2 = "999998"
    else:
        near1 = str(int(pr1) + 1).zfill(6)
        near2 = str(int(pr1) - 1).zfill(6)
    if me[-2:] == back2:
        money += 2000
    if me[:3] == font3_1 :
        money += 4000
    if me[:3] == font3_2:
        money += 4000
    if me[-3:] == back3_1:
        money += 4000
    if me[-3:] == back3_2:
        money += 4000
    if me == near1:
        money += 100000
    if me == near2:
        money += 100000
    if me == pr1:
        money+=6000000
    print(int(money))
main()
