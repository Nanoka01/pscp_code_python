"""Saint Seiya"""
def main(x = int(input()), y = int(input())):
    """Saint Seiya"""
    punch = 0
    rolling_crash = False
    for i in range(1,x+1):
        if not rolling_crash:
            if punch >= y:
                rolling_crash = True
                continue
        if not i%2 and not rolling_crash:
            if not i%6:
                punch += 1
            else:
                punch += 165
            continue
        if rolling_crash:
            punch += (x-i+1)*12
            break
    print(punch)
main()
