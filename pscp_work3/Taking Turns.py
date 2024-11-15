"""Taking Turns"""
import json
def main():
    """wqserfdas"""
    lst = json.loads(input())
    total =[]
    if lst:
        total.append(lst.pop(-1))
    while lst:
        if lst:
            total.append(lst.pop(0))
        if lst:
            total.append(lst.pop(0))
        if lst:
            total.append(lst.pop(-1))
        if lst:
            total.append(lst.pop(-1))
    print(total)
main()
