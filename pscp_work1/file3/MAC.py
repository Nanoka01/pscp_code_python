"""MAC"""
def main(txt):
    """MAC"""
    num = '0123456789ABCDEFabcdef'
    txts = txt.replace('-','')
    txts = txts.replace(':','')
    txts = txts.replace('.','')
    if len(txts) != 12:
        print('ERROR')
        return
    if len(txt) in (14,17):
        for i in txts:
            if not i in num:
                print('ERROR')
                return
        if len(txt) == 17:
            if txt[2] == '-' and txt[5] == '-' and txt[8] == '-' \
                and txt[11] == '-' and txt[14] == '-':
                txt = txt.replace('-','')
                print('VALID 1')
            elif txt[2] == ':' and txt[5] == ':' and txt[8] == ':' \
                and txt[11] == ':' and txt[14] == ':':
                print('VALID 2')
            else:
                print('ERROR')
        if len(txt) == 14:
            if txt[4] == '.' and txt[9] == '.':
                print('VALID 3')
            else:
                print('ERROR')
    else:
        print('ERROR')
main(str(input()))
