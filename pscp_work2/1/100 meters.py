"""100 meters"""
def main():
    """Midterm"""
    a, b, c = 0, 0, 0
    first, second, third = 0, 0, 0
    time = 0
    for i in range(1,9) :
        time = float(input())
        if time < a or not a :
            a,b,c = time,a,b
            first,second,third = i,first,second
        elif time < b or not b :
            b,c = time,b
            second,third = i,second
        elif time < c or not c :
            c = time
            third = i
    print(first,second,third)
main()
