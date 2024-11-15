"""LineSorting"""
def main():
    """main"""
    t_list=  []
    a= []
    num = int(input())
    for _ in range(num):
        txt = input()
        t_list.append(txt)

    while True:
        a.append(min(t_list, key=len))
        t_list.remove(min(t_list, key=len))
        len_t = len(t_list)
        if not len_t:
            break
    for i in a:
        print(i)
main()
