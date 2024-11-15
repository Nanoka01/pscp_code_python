"""ชีวะจักรโบราณ"""
def main(num):
    """main"""
    if num==0:
        print("zezeso")
    elif num==1:
        print("papan")
    elif num==2:
        print("dogugu")
    elif num==3:
        print("gushigi")
    elif num==4:
        print("zugogo")
    elif num==5:
        print("zugagi")
    elif num==6:
        print("gibugu")
    elif num==7:
        print("gezun")
    elif num==8:
        print("gegido")
    elif num==9:
        print("bagin")
    else:
        return num

def upnum(num):
    txt = ["zezeso","papan","dogugu","gushigi","zugogo","zugagi","gibugu","gezun","gegido","bagin"]
    ch = 1
    x = ""
    if num>9:
        if num <= 18:
            for i in range(1,10):
                if 9+i==num:
                    print("bagindo",txt[i-10])
        else:
            if num>=81:
                while True:
                    if ch*9>=num:
                        break
                    else:
                        ch*=9
                        x+=txt[8]
num = int(input())
main(num)
upnum(num)
