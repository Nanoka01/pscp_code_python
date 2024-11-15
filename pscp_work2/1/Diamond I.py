"""Diamond"""
def main(y = int(input()), x = int(input())):
    """Diamond"""
    mine = {}
    value_list = []
    for i in range(1,y+1):
        mine[i] = (input().split())
    for i in range(x):
        value = 0
        for j in range(1,y+1):
            value += int(mine[j][i])
            if j == y:
                value_list.append(value)
    value_list.sort(reverse=True)
    print(value_list[0])
main()

