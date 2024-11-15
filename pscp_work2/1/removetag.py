"""RemoveTag"""
def main(x = str(input())):
    """RemoveTag"""
    result = ""
    inside_tag = False
    for i in x:
        if i == "<":
            inside_tag = True
            result += " "
        elif i == ">":
            inside_tag = False
            continue
        if not inside_tag:
            result += i
    print(result.split())
main()
