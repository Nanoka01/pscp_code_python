"""Real"""
def main():
    """a"""
    a_s=""
    total=""
    int_t = ""
    co=0
    for _ in range(3):
        a0=input()
        a1=input()
        a2=input()
        a3=input()
        a4=input()
        a5=input()
        a6=input()
        a7=input()
        a_s=a0+a1+a2+a3+a4+a5+a6
        if a_s=="ononononononoff":
            total+="0"
        elif a_s=="offononoffoffoffoff":
            total+="1"
        elif a_s=="ononoffononoffon":
            total+="2"
        elif a_s=="ononononoffoffon":
            total+="3"
        elif a_s=="offononoffoffonon":
            total+="4"
        elif a_s=="onoffononoffonon":
            total+="5"
        elif a_s=="onoffononononon":
            total+="6"
        elif a_s=="onononoffoffoffoff":
            total+="7"
        elif a_s=="ononononononon":
            total+="8"
        elif a_s=="ononononoffonon":
            total+="9"
        else:
            co=-1
        if a7=="on":
            total+="."
        a_s=""
    if co==-1:
        print("Error")
        return
    elif (total[0])=="0" and (total[1])!=".":
        for i in total:
            if i!=".":
                int_t+=i
        int_t=int(int_t)
        int_t=len(str(int_t))
        print("Error")
    else:
        f=float(total)
        print(f"{f:.2f}")
main()
