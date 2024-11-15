"""BloodDonation"""
def main():
    """dasd"""
    age = int(input())
    wigth = int(input())
    num_blood = int(input())
    if age == 17 or 60 <= age <= 70:
        y_n = input()
        if y_n=="False":
            return "No"
    if age<17 or age>70:
        return "No"
    if wigth <45:
        return "No"
    if not num_blood and age>55:
        return "No"
    return "Yes"
print(main())
