"""Post Office"""
def main():
    """vcvc"""
    n = int(input())
    m = int(input())
    s_n = 0
    s_m = 0
    for _ in range(n):
        wi = float(input())
        if wi>1000:
            s_n+=68
        elif wi>500:
            s_n+=48
        elif wi>250:
            s_n+=33
        elif wi>100:
            s_n+=28
        elif wi>20:
            s_n+=23
        elif wi>10:
            s_n+=18
        else:
            s_n+=16
    s_n=s_n+(n*13)
    for _ in range(m):
        wi=float(input())
        if wi>1000:
            s_m+=70
        elif wi>500:
            s_m+=55
        else:
            s_m+=45
    s_m=s_m+(m*15)
    print(s_m+s_n)
main()
