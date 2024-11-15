"""Longer"""
import math
def main():
    """main"""
    pir = math.pi
    r = float(input())
    a = float(input())
    b = float(input())
    circle = 2*pir*r
    rectangle = (2*a)+(2*b)
    total = abs(circle-rectangle)
    total = f"{total:.5f}"
    if circle > rectangle:
        print("Circle is longer")
    elif circle == rectangle:
        print("Equal")
    else:
        print("Rectangle is longer")
    print(total)
main()
