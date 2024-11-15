"""game"""
def main():
    """adsfas"""
    score_A = int(input())
    score_B = int(input())
    if score_A < 0 or score_B < 0:
        print("Error")
        return
    diff = abs(score_A - score_B)
    if not diff % 3:
        draws = max(score_A - (score_A // 3) * 3, score_B - (score_B // 3) * 3)
        print(draws)
    else:
        print("Error")
main()
