"""Home Run"""
def main():
    """main"""
    n = int(input())
    player = float(input())
    cou = 0
    for _ in range(n):
        a = float(input())
        if a < player:
            cou+=1
    print(cou)
main()
