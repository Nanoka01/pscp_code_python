"""seeker"""
def main():
    """main"""
    txt = input()
    s_num = ""
    total = 0
    for i in txt:
        if i.isnumeric():
            s_num += i
        else:
            if s_num:
                total += int(s_num)
                s_num = ""
    if s_num:
        total += int(s_num)
    print(total)
main()
