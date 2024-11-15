"""stamps"""
def main():
    """main"""
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    total = 0
    stamps = 0
    for _ in range(n):
        bill = int(input())
        while stamps >= c:
            if bill <= d:
                stamps -= c
                bill = 0
                break
            else:
                stamps -= c
                bill -= d
        total += bill
        if bill > 0:
            new_stamps = (bill // a) * b
            stamps += new_stamps
    print(total)
    print(stamps)
main()
