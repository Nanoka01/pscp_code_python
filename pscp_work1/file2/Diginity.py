"""Diginity"""
def main():
    """main"""
    num = ""
    total = []
    n = 0
    while True:
        num = str(int(input()))
        if num == "0":
            break
        while True:
            n=0
            for i in num:
                i=int(i)
                n+=i
            num=str(n)
            if len(str(n))==1:
                total.append(n)
                n = 0
                break
    for i in total:
        print(i)
main()
