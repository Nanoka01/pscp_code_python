"""Counting Stars"""
def main():
    """isusus eyee tum ma 4 day kwa ja sed yed mem left to right  i sus"""
    star = input()

    totalconstellation = 0
    totalcomet = 0
    totalshootingstar =0
    star = star.strip()
    frist = ""
    second = ""

    while True:
        if star.find("**") == -1 and star.find("~*") == -1:
            if  star.find("*~") == -1 and star.find("*/") == -1:
                break

        for char in star:
            second = frist
            frist = char
            word = second + frist
            if word == "~*":
                totalcomet = totalcomet+1
                star = star.replace("~*"," ",1)
                frist = ""
                second = ""
                break
            if word == "*~":
                totalcomet = totalcomet+1
                star = star.replace("*~"," ",1)
                frist = ""
                second = ""
                break
            if word == "*/":
                totalshootingstar = totalshootingstar+1
                star = star.replace("*/"," ",1)
                frist = ""
                second = ""
                break
            if word == "**":
                totalconstellation = totalconstellation+1
                star = star.replace("**"," ",1)
                frist = ""
                second = ""
                break

    if not totalconstellation and not totalcomet and not totalshootingstar:
        print("Tonight is a quiet night.")
    else:
        print(f"constellation: {totalconstellation}")
        print(f"comet: {totalcomet}")
        print(f"shooting star: {totalshootingstar}")

main()
