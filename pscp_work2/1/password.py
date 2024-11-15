"""emc2"""
import math
def main(password):
    """DESDASDSA"""
    smalla = "abcdefghijklmnopqrstuvwxyz"
    biga = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    extra = "=+#$%^&*@_![{()}]"
    number = "0123456789"
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    for i in (password):
        if i in smalla:
            r1 = 26
        if i in biga:
            r2 = 26
        if i in extra:
            r3 = 32
        if i in number:
            r4 = 10
    r = r1+r2+r3+r4
    l = len(password)
    e = int(math.log2(r**l))
    if e < 28 :
        print(e)
        print("Very Weak")
    elif 28<=e<=35:
        print(e)
        print("Weak")
    elif 36<=e<=59:
        print(e)
        print("Reasonable")
    elif 60<=e<=127:
        print(e)
        print("Strong")
    else:
        print(e)
        print("Very Strong")
main(input())
