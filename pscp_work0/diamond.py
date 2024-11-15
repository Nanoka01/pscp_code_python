"""diamond"""
Row = int(input())

if Row == 1:
    print("*")
else:
    Rowupper = (Row-1) //2
    k=0
    for i in range(Rowupper):
        print(" ",end="")
    print("*")

    for i in range(Rowupper-1):
        for j in range(1,Rowupper-k):#print whitespace
            j =j*1
            print(" ",end="")
        print("*",end="")
        for j in range(1+(2*k)):
            j=j*1
            print(" ",end="")
        print("*",end="")
        k=k+1
        print("")

    for l in range(Row):
        l=l*1
        print("*",end="")
    print("")

    k = k-1
    for i in range(Rowupper-1):
        for j in range(1+i):#print whitespace
            j=j*1
            print(" ",end="")
        print("*",end="")
        for j in range(1+(2*k)):
            j=j*1
            print(" ",end="")
        print("*",end="")
        k=k-1
        print("")

    for i in range(Rowupper):
        print(" ",end="")
    print("*")
