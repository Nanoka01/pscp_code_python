"""Niwarn World"""
import math

def x(n):
    """x"""
    return 2 + (math.log2(n**2)) / (2 * n * math.log2(n))

def y(n, s):
    """y"""
    return ((math.sin(math.radians(30)) + (math.sqrt(2 * s))) / (x(n) + 3))

def z(k):
    """z"""
    return y(k, k)**2 + (8456 * x(k)**4) / (24 * k)

def main():
    """Main"""
    n = float(input())
    s = float(input())
    k = float(input())

    x_value = x(n)
    y_value = y(n,s)
    z_value = z(k)

    print(f"X: {x_value:.1f}, Y: {y_value:.1f}, Z: {z_value:.1f}")

main()
