"""Sciencific Notation"""
def to_nu(text) :
    """Change Normal to Sciencific Notation form"""
    left = text[:text.find(".")].strip()
    right = text[text.find(".")+1:].strip()
    count = 0
    if 1 <= float(text) < 10 :
        return f"{left}"+f".{right}"*bool(right)+ f" x 10^{count}"
    if float(text) >= 10 :
        count = len(left)-1
        if not right :
            left = str(int(left[::-1]))[::-1]
        left = left.replace(".","")
        return f"{left[0]}"+"."*bool(len(left)>1)+\
            f"{left[1:]}{right} x 10^{count}"
    for i in right :
        count += 1
        if i not in "0" :
            break
    right = str(int(right))
    return f"{right[0]}"+"."*bool(len(right)>1)+f"{right[1:]} x 10^-{count}"

def check(text) :
    """Change Sciencific Notation to Normal form"""
    if text.find(".",0,text.find("x")) == -1 :
        text = text[0:text.find("x")].strip() + "." + text[text.find("x"):].strip()
    left = text[:text.find(".")].strip()
    right = text[text.find(".")+1:text.find("x")].strip()
    count = text[text.find("^")+1:].strip()
    if int(count) < 0 :
        left = "0"*abs(int(count)) + left
        return f"{left[0]}.{left[1:]}{right}"
    if int(count) > 0 :
        right = f"{right:<0{int(count)}}"
        return f"{left}{right[:int((count))]}.{right[int(count):]}"
    return left+"."+right

def main() :
    """main"""
    text = str(input())
    deleted = False
    cal = None
    if text[0] in "-" :
        deleted = True
        text = text[1:]
    if text.count("x") > 0 :
        cal = check(text)
    else :
        text += "."*(text.count(".") < 1)
        if not float(text) :
            print(0)
            return
        cal = to_nu(text)
    if not cal[cal.find(".")+1:] :
        cal = cal.replace(".","")
    print("-"*deleted+cal)
main()
