"""IT Business"""
def main(bank, cash):
    """IT Business"""
    error = 0
    while error != 3:
        x = input()
        if x == 'end':
            break
        statement = x[0]
        money = float(x[2:len(x)])
        if statement == 'D':
            if cash < money:
                error += 1
            else:
                bank += money
                cash -= money
                error = 0
        elif statement == 'W':
            if bank < money:
                error += 1
            else:
                bank -= money
                cash += money
                error = 0
    print(f'{bank:.2f}\n{cash:.2f}')
main(float(input()), float(input()))
