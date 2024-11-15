"""Niwarn World"""
def main():
    """mian"""
    total = ""
    txt = input()
    x = txt.replace("13", "B")
    txt = x
    x = txt.replace("12","R")
    txt = x
    x = txt.replace("0","O")
    txt = x
    x = txt.replace("5","S")
    txt = x
    x = txt.replace("4","A")
    txt = x
    x = txt.replace("3","E")
    txt = x
    x = txt.replace("1","I")
    txt = x.upper()
    for i in txt:
        if not i.isnumeric():
            total+=i
    print(total)
main()
