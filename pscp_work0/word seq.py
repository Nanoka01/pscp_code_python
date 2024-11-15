"""WordSequence I"""
def main():
    """WordSequence I"""
    messenger = input()
    length_messenger = len(messenger)
    for i in range(length_messenger):
        print(messenger[:i+1])
main()
