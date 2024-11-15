"""Muddled Menu"""
def main():
    """adsaf"""
    menu = []
    ch = 0
    while True:
        txt = input()
        if txt[-2]=="#":
            if txt[-1]=="N":
                menu.append(txt[:-2].strip())
            else:
                menu.insert((int(txt[-1])-1),txt[:-2].strip())
        elif txt[:9] == "Can't do:":
            item_to_remove = txt[10:].strip()
            if item_to_remove in menu:
                menu.remove(item_to_remove)
        elif txt =="SOMETHING'S WRONG":
            menu.clear()
        elif txt=="CLOSED":
            ch = -1
            menu.clear()
            break
        elif txt =="DONE":
            break
    if ch == -1:
        print("Full Course: [] Reversed: []")
    else:
        print(f"Full Course: {menu} Reversed: {menu[::-1]}")
main()
