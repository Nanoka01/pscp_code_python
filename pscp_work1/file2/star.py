"""Counting Stars"""
def main():
    """main"""
    txt = input()
    constellation = 0
    comet = 0
    shooting_star = 0
    i = 0
    while i < len(txt):
        if txt[i:i+2] == "**":
            constellation += 1
            i += 2
        elif txt[i:i+2] == "~*" or txt[i:i+2] == "*~":
            comet += 1
            i += 2
        elif txt[i:i+2] == "*/":
            shooting_star += 1
            i += 2
        else:
            i += 1
    if not comet and not shooting_star and not constellation:
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {constellation}")
        print(f"comet: {comet}")
        print(f"shooting star: {shooting_star}")
main()
