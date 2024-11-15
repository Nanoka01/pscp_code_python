def main():
    """Tuple Exercise"""
    # รับค่าทั้งหมดใน Tuple
    values = tuple(input().split())
    
    # รับค่าเป้าหมาย
    target = input()
    
    # หาตำแหน่งแรกของค่าใน Tuple
    first_index = values.index(target)
    
    # นับจำนวนครั้งที่ค่าปรากฏใน Tuple
    count = values.count(target)
    
    # วาดรูปสี่เหลี่ยมจตุรัสตามจำนวนที่นับได้
    for _ in range(count):
        print(f"{first_index} " * count)

main()
