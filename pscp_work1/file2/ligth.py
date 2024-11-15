"""Bonus"""
def main():
    """main"""
    money = int(input())
    year = int(input())
    mouth = int(input())
    if mouth>=10:
        year+=1
    if year>20:
        year=20
    total=money*year
    if total < 5000:
        total=5000
    print(total)
main()
                    