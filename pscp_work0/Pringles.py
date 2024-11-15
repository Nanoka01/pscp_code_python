"""Pringles"""
box1 =  input()
chips = input()
box2 =input()
fingerlong = int(input())

COUNTCHIPS = 0
PICK=0
run = fingerlong
for i in range(fingerlong):
    i=i*1
    for char in chips:
        if not run:
            break
        if char == ")":
            chips = chips.replace(")"," ",1)
            PICK = PICK+1
        run = run-1
COUNTCHIPS = chips.count(")")

if COUNTCHIPS > 0:
    print(PICK)
    print("There are still some left.")
else:
    print(PICK)
    print("None.")
print(box1)
print(chips)
print(box2)
