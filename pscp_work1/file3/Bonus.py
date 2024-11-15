"""bonus"""
def main():
    """main"""
    salary = int(input())
    years = int(input())
    months = int(input())
    if months >= 10:
        years += 1
    if years > 20:
        years = 20
    bonus = salary * years
    if bonus < 5000:
        bonus = 5000
    elif bonus > 1000000:
        bonus = 1000000
    print(bonus)
main()
