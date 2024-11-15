"""Supercar Parking"""
def main():
    """Supercar Parking"""
    txt = list(input())
    count = 0
    if len(txt) > 1 and txt[0] == "0" and txt[1] == "0":
        count += 1
        txt[0] = "1"

    for i in range(1, len(txt) - 1):
        if txt[i] == "0" and txt[i - 1] == "0" and txt[i + 1] == "0":
            count += 1 
            txt[i] = "1"

    if len(txt) > 1 and txt[-1] == "0" and txt[-2] == "0":
        count += 1
        txt[-1] = "1"

    if len(txt) == 1 and txt[0] == "0":
        count += 1
    print(count)
main()
