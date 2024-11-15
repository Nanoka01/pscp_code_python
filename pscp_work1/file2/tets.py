"""Harshad"""
def main():
    """Ch"""
    total = []
    for _ in range(10):
        number = int(input())
        number = abs(number)
        digit_sum = sum(int(digit) for digit in str(number))
        if not number:
            total.append("No")
        elif not digit_sum:
            total.append("No")
        elif not number % digit_sum:
            total.append("Yes")
        else:
            total.append("No")
    for i in total:
        print(str(i))
main()
