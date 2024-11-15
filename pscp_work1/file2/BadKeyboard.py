"""Easy Histogram"""
def main():
    """main"""
    text = input().split(" ")
    text = "".join(text)
    print(text)
    total = []
    cou = 0
    sorted_text = "".join(sorted(text, key=lambda x: (x.lower(), x.isupper())))
    print(sorted_text)
    for i in range(len(sorted_text)):
        if sorted_text[i+1]==sorted_text[i]:
            cou+=1
        else:
            print(f"{sorted_text[i]} = {cou}")
            cou = 0
main()
