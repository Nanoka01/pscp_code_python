"""coffee"""
def main():
    """asd"""
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = int(input())
    if e == 1:
        price1 = a
    else:
        price1 = a + (e - 1) * a * (1 - b / 100)
    total_price = e * a
    if total_price >= d:
        price2 = total_price * (1 - c / 100)
    else:
        price2 = total_price
    if price1 < price2:
        print(1)
        print(f"{price1:.2f}")
    else:
        print(2)
        print(f"{price2:.2f}")

main()
