"""Amefuri Plus"""
def whentheshirtdry():
    """whentheshirtdry"""
    time = int(input())
    weather = input()
    wet = 8
    Lost = False
    for nowweather in weather:
        if nowweather in ('C', 'c'):
            if  6 <= time < 18:
                wet = wet - 0.50
            else:
                wet = wet - 0.25

        if nowweather in ('N', 'n'):
            if  6 <= time < 18:
                wet = wet - 1.00
            else:
                wet = wet - 0.50

        if nowweather in ('W', 'w'):
            if 6 <= time < 18:
                wet = wet - 1.50
            else:
                wet = wet - 0.75

        elif nowweather in ('R', 'r'):
            wet = wet + 2.00

        elif nowweather in ('S', 's'):
            wet = wet + 3.00

        elif nowweather in ('H', 'h'):
            Lost = True
            break

        time = time+1
        if time > 24:
            time = 1

        if wet > 16:
            wet = 16
        elif wet <= 0:
            break

    if Lost is True:
        print("Lost")
    elif wet <= 0:
        print("Dry")
    else:
        print(f"Still Wet (Wet Level: {wet:.2f})")

whentheshirtdry()
