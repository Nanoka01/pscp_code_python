"""B - Fully pair?"""
def main():
    """main"""
    letters = input()
    counts = {}
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    unpaired_letters = ""
    for letter in letters:
        if counts[letter] % 2 and letter not in unpaired_letters:
            unpaired_letters += letter
    if not unpaired_letters:
        print("fully paired")
    else:
        print(unpaired_letters)
main()
