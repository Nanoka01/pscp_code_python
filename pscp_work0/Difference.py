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
    for i in sorted(e_a - e_b):
        print(i, end=" ")
differen()
