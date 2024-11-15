"""A"""
def main():
    """A"""
    text = input()

    two_grams = []
    count = {}

    for i in range(len(text) - 1):
        gram = text[i] + text[i + 1]

        two_grams.append(gram)

    for j in two_grams:
        if j in count:
            count[j] += 1
        else:
            count[j] = 1

    max_key = max(count, key=count.get)
    max_value = count[max_key]
    print(max_key)
    print(max_value)

main()
