"""Amefuri Plus"""
def main():
    """main"""
    Wet = 8
    H = int(input())
    wt = input()
    for i in wt:
        if i in ("H","h"):
            print("Lost")
            break
        if 6 <= H < 18:
            if i in ("C", "c"):
                Wet -= 0.5
            elif i in ("N", "n"):
                Wet -= 1
            elif i in ("W", "w"):
                Wet -= 1.5
        else:
            if i in ("C", "c"):
                Wet -= 0.25
            elif i in ("N", "n"):
                Wet -= 0.5
            elif i in ("W", "w"):
                Wet -= 0.75
        if i in ("R","r"):
            Wet+=2
        elif i in ("S","s"):
            Wet+=3
        if Wet<=0:
            print("Dry")
            break
        Wet = max(0, min(Wet, 16))
        H = (H + 1) % 24
    if Wet > 0 and i not in ("H","h"):
        print(f"Still Wet (Wet Level: {Wet:.2f})")
main()
