"""iPhone 13 Again"""
def main():
    """nain"""
    mini13=[25900,29900,37900]
    nor13=[29900,33900,41900]
    pro13=[38900,42900,50900,58900]
    max13=[42900,46900,54900,62900]
    name = input()
    memo = input()
    if name =="iPhone 13 mini":
        if memo=="128 GB":
            print(mini13[0])
        elif memo=="256 GB":
            print(mini13[1])
        elif memo=="512 GB":
            print(mini13[2])
        else:
            print("Not Available")
    elif name =="iPhone 13":
        if memo=="128 GB":
            print(nor13[0])
        elif memo=="256 GB":
            print(nor13[1])
        elif memo=="512 GB":
            print(nor13[2])
        else:
            print("Not Available")
    elif name=="iPhone 13 Pro":
        if memo=="128 GB":
            print(pro13[0])
        elif memo=="256 GB":
            print(pro13[1])
        elif memo=="512 GB":
            print(pro13[2])
        elif memo=="1 TB":
            print(pro13[3])
        else:
            print("Not Available")
    elif name=="iPhone 13 Pro Max":
        if memo=="128 GB":
            print(max13[0])
        elif memo=="256 GB":
            print(max13[1])
        elif memo=="512 GB":
            print(max13[2])
        elif memo=="1 TB":
            print(max13[3])
        else:
            print("Not Available")
    else:
        print("Not Available")
main()
