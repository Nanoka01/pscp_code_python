"""Lift"""
def main():
    """main"""
    num = int(input())
    wight = float(input())
    man = 0
    total_w =0
    for _ in range(num):
        a = int(input())
        b = float(input())
        if a >=12:
            man+=1
        total_w+=b
    if man>0 and total_w <= wight:
        print("Safe")
    elif not num:
        print("Safe")
    else:
        print("Not Safe")
main()
