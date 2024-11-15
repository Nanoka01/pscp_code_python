"""Stuttering"""
def main():
    """sget"""
    last_word = ""
    result = []
    words = input().split()
    for word in words:
        if word != last_word:
            result.append(word)
        last_word = word

    print(" ".join(result))
main()
