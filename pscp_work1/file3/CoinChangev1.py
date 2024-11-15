"""A"""
def main():
    """A"""
    num = int(input())
    x = 0
    y = 0
    z = 0
    a = 0

    while num > 0:
        if num >= 25:
            x += num // 25
            num -=(x * 25)
        elif num >= 10:
            y += num // 10
            num -=(y * 10)
        elif num >= 5:
            z += num // 5
            num -=(z * 5)
        else:
            a += num // 1
            num -=(a * 1)

    print(x+y+z+a)

main()
