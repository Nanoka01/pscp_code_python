"""dimond"""
def main():
    """main"""
    num = int(input())
    num1 = num // 2
    print(" " * num1 + "*")
    for i in range(1, num1):
        print(" " * (num1 - i) + "*" + " " * (2 * i - 1) + "*")
    print("*" * num)
    for i in range(num1 - 1, 0, -1):
        print(" " * (num1 - i) + "*" + " " * (2 * i - 1) + "*")
    print(" " * num1 + "*")
main()
