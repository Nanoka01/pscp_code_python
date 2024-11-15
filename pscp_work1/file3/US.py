"""US Interstate Number System"""
def main(rodeo = str(input())):
    """US Interstate Number System"""
    result = 'I-'
    if len(rodeo) == 2 or len(rodeo) == 1:
        for i in rodeo:
            last = i
        rodeo = str(int(rodeo))
        if last == '0' and rodeo != '0':
            print(f'Horizontal Major Interstate\n{result+rodeo}')
        elif last == '5' and rodeo != '0':
            print(f'Vertical Major Interstate\n{result+rodeo}')
        else:
            print('Others')
    elif len(rodeo) == 3:
        for i in rodeo:
            first = i
            rodeo = rodeo.replace(first,'',1)
            break
        for i in rodeo:
            last = i
        if last in ('0','5') and 5 <= int(rodeo) <= 95:
            if not int(first)%2:
                print(f'Even Minor Interstate\n{result+rodeo}')
            elif int(first)%2:
                print(f'Odd Minor Interstate\n{result+rodeo}')
        else:
            print('Others')
main()
