"""Bonus"""
def main():
    """main"""
    salary = int(input())
    years = int(input())
    months = int(input())
    if months >= 10:
        years += 1
    if years > 20:
        years = 20
    total_bonus = salary * years
    if total_bonus < 5000 and salary > 0:
        total_bonus = 5000
    elif total_bonus > 1000000:
        total_bonus = 1000000
    print(total_bonus)
main()
