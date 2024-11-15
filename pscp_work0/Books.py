"""Books"""
import math
def findaday():
    """findaday"""
    Number_of_volumes = int(input())
    Number_page = int(input())
    x = int(input())
    y = int(input())
    i =0
    readpage = 0
    Nowpage = Number_page
    day = 0
    count_bookinllop =0
    while True:
        readpage = math.ceil(((x+i)/(y+i))*Number_page)
        if not Number_of_volumes:
            break
        if readpage >= Number_page:
            break
        Nowpage = Nowpage-readpage
        if Nowpage <= 0:
            Number_of_volumes = Number_of_volumes-1
            Nowpage = Number_page
        i=i+1
        day = day+1
    if  Number_of_volumes > 0:
        day = day +(Number_of_volumes-count_bookinllop)
    print(day)
findaday()
