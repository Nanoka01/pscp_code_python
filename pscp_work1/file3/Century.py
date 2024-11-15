"""Century"""
import math
def main():
    """main"""
    num = int(input())
    n = 0
    total = []
    for _ in range(num):
        year = input()
        n = int(year[5:])
        if year[0:4]=="B.E.":
            if n <=543:
                total.append("ERROR")
            else:
                n-=543
                n = math.ceil(n/100)
                total.append(n)
        else:
            n = math.ceil(n/100)
            total.append(n)
    for i in total:
        print(i)
main()
