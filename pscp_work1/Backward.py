"""Backward"""
def main():
    """f"""
    total = []
    a = []
    txt =""
    while txt != "NULL":
        txt = input()
        if txt != "NULL":
            total.append(txt)
        else:
            break
    a = total[::-1]
    for i in a:
        print(i)
main()
