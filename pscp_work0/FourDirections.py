"""FourDirections"""
Word = input()
for char in Word:
    print("  *  ",end=" ")
print("")
for char in Word:
    if char == "U":
        print(" *** ",end=" ")
    elif char == "D":
        print("  *  ",end=" ")
    elif char == "L":
        print(" *   ",end=" ")
    elif char == "R":
        print("   * ",end=" ")
print("")
for char in Word:
    if char == "U":
        print("* * *",end=" ")
    elif char == "D":
        print("* * *",end=" ")
    elif char == "L":
        print("*****",end=" ")
    elif char == "R":
        print("*****",end=" ")
print("")
for char in Word:
    if char == "U":
        print("  *  ",end=" ")
    elif char == "D":
        print(" *** ",end=" ")
    elif char == "L":
        print(" *   ",end=" ")
    elif char == "R":
        print("   * ",end=" ")
print("")
for char in Word:
    print("  *  ",end=" ")
