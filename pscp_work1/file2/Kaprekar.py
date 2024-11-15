"""Kaprekar"""
def main():
    """main"""
    a = input().strip()
    numx = a
    cou = 0
    while True:
        numbers = [int(digit) for digit in numx]
        numbers.sort(reverse=True)
        numx = ''.join(map(str, numbers))
        numbers.sort()
        numn = ''.join(map(str, numbers)).zfill(4)
        total = int(numx) - int(numn)
        print(total)
        if total == 6174:
            break
        numx = str(total).zfill(4)
        cou += 1
    print(cou)
main()
