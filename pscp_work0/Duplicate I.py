'''diff'''
def differen():
    '''ddddddd'''
    a = int(input())
    b = int(input())
    e_a = set()
    e_b = set()
    for _ in range(a):
        e_a.add(int(input()))
    for _ in range(b):
        e_b.add(int(input()))
    if sorted(e_a.intersection(e_b)):
        for i in sorted(e_a.intersection(e_b),reverse=True):
            print(i)
    else:
        print("Nope")
differen()
