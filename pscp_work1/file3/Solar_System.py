"""Solar System"""
from math import ceil
def evenstar(sun_num, star_num, hot, first, current):
    """When Star count is Even"""
    if sun_num > ceil(star_num/2):
        print(f'Hot: {hot}\nCool: {first}')
    if sun_num <= ceil(star_num/2):
        print(f'Hot: {hot}\nCool: {current}')

def oddstar(sun_num, star_num, hot, first, current):
    """When Star count is odd"""
    if sun_num > ceil(star_num/2):
        print(f'Hot: {hot}\nCool: {first}')
    elif sun_num < ceil(star_num/2):
        print(f'Hot: {hot}\nCool: {current}')
    else:
        print(f'Hot: {hot}\nCool: {first}{current}')

def main(solar = str(input())+' '):
    """Solar System"""
    prev = ''
    current = ''
    star = ''
    star_num = solar.count(' ')
    num = 0
    sun_num = 0
    first = ''
    hot = ''
    for i in solar:
        star += i
        if i == ' ':
            first = star
            star = ''
            break
    for i in solar:
        if i != ' ':
            star += i
        else:
            prev = current
            current = star
            star = ''
            num += 1
            if current == 'Sun':
                sun_num = num
                if prev:
                    hot += f'{prev} '
                else:
                    hot += prev
            if prev == 'Sun':
                hot += current
    if not star_num%2:
        evenstar(sun_num, star_num, hot, first, current)
    else:
        oddstar(sun_num, star_num, hot, first, current)
main()
