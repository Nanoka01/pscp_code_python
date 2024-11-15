"""DNA"""
def main(dna1 = str(input()), dna2 = str(input())):
    """DNA"""
    pool = 'ACGT'
    if any(i not in pool for i in dna1) or any( j not in pool for j in dna2):
        print('Error')
        return
    longest = ''
    if len(dna1) > len(dna2):
        dna1, dna2 = dna2, dna1
    len1 = len(dna1)

    for start in range(len1):
        for end in range(start+1,len1+1):
            substring = dna1[start:end]
            if substring in dna2:
                if len(substring) > len(longest):
                    longest = substring
    print(longest if longest else 'None')
main()
