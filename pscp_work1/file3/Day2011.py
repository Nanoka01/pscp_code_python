"""A"""
def main():
    """A"""
    d = int(input())
    m = int(input())

    day_list = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    mount_dict = {1: 0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:212, 9:243, 10:273, 11:304, 12:334}

    day_check = (d + mount_dict[m]) // 7
    day_collect = day_list[day_check - 1]

    print(day_collect)

main()
