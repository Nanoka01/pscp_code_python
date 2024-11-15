"""Bubble"""
def main() :
    """Bubble"""
    runaway = input() + "||||"
    i = 0
    step = 0
    while runaway[i] != "|" :
        if runaway[i] == "^" :
            if runaway[i+1] != " " :
                i += 1
                step += 1
            else :
                print("IMPOSSIBLE")
                print(runaway.find("|")-i)
                return
        elif runaway[i] == "o" :
            if runaway[i+1] != " " :
                i += 1
                step += 1
            else :
                if runaway[i-1] in "O" and runaway[i+1:i+4] not in "   " :
                    i -= 1
                else :
                    print("IMPOSSIBLE")
                    print(runaway.find("|")-i)
                    return
        elif runaway[i] in "O" and runaway[i+1:i+4] not in "   " :
            for far in range(3,0,-1) :
                if runaway[i+far] not in " " :
                    i += far
                    step += 1
                    break
        else :
            print("IMPOSSIBLE")
            print(runaway.find("|")-i)
            return
    print("POSSIBLE")
    print(step)
main()
