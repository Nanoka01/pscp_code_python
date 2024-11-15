"""A"""
def main():
    """A"""
    num = int(input())
    count = 0

    for i in range(1, num + 1):
        if not i % 3 or not i % 5:
            count += i

    print(count)

main()
