"""Real"""
def dec_7_seg():
    """Decode 7-Segment"""
    state = ''
    state += '1' if str(input()) == 'on' else '0'
    state += '1' if str(input()) == 'on' else '0'
    state += '1' if str(input()) == 'on' else '0'
    state += '1' if str(input()) == 'on' else '0'
    state += '1' if str(input()) == 'on' else '0'
    state += '1' if str(input()) == 'on' else '0'
    state += '1' if str(input()) == 'on' else '0'
    dp = 1 if str(input()) == 'on' else 0

    l0 = '1111110'
    l1 = '0110000'
    l2 = '1101101'
    l3 = '1111001'
    l4 = '0110011'
    l5 = '1011011'
    l6 = '1011111'
    l7 = '1110000'
    l8 = '1111111'
    l9 = '1111011'

    led = ''
    if state == l0:
        led += '0'
    elif state == l1:
        led += '1'
    elif state == l2:
        led += '2'
    elif state == l3:
        led += '3'
    elif state == l4:
        led += '4'
    elif state == l5:
        led += '5'
    elif state == l6:
        led += '6'
    elif state == l7:
        led += '7'
    elif state == l8:
        led += '8'
    elif state == l9:
        led += '9'
    else:
        led += 'Er'
    if dp:
        led += '.'
    return led

def main():
    """Real"""
    signal = ''
    for _ in range(3):
        signal += dec_7_seg()
    if signal.count('.') > 1 or signal.count('Er') >= 1:
        print('Error')
    else:
        print(f'{float(signal):.2f}')
main()
