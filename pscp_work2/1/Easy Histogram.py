"""Tuple's Sad life"""
def main():
    """Tu"""
    values = tuple(input().split())
    target = input()
    first_index = values.index(target)
    count = values.count(target)
    for _ in range(count):
        print(f"{first_index} " * count)

main()
