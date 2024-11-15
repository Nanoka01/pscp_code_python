"""jfkld"""
def main():
    """main"""
    n = int(input())
    my_list = []
    for _ in range(n):
        r = float(input())
        my_list.append(r)
        my_list.sort()
    med = (n+1)/2
    if not n%2:
        med1 = int(med+0.5)
        med2 = int(med-0.5)
        total = (my_list[med1-1]+my_list[med2-1])/2
        print(f"{total:.3f}")
    else:
        med = int(med)
        print(f"{my_list[med-1]:.3f}")
main()
