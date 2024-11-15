"""AndAgainAndAgain..."""
def main(text = input()):
    """AndAgainAndAgain..."""
    text = text.replace('.','')
    text = text.split()
    vowel_pool = ('a','e','i','o','u','A','E','I','O','U')
    result = []
    for i in text:
        vowel_count = 0
        for j in str(i):
            if j in vowel_pool:
                vowel_count += 1
            if vowel_count >= 2:
                result.append(i)
                vowel_count = 0
                break
    result.sort()
    if result:
        for i in result:
            print(i)
    else:
        print("Nope")
main()
