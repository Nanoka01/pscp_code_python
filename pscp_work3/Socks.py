def main():
    socks = input().strip()
    
    # สร้างลิสต์ขนาด 26 สำหรับเก็บจำนวนถุงเท้าแต่ละตัว (A ถึง Z)
    count = [0] * 26
    
    # นับจำนวนถุงเท้าแต่ละตัว
    for sock in socks:
        count[ord(sock) - ord('A')] += 1
    
    result = []
    total_pairs = 0
    
    # วนลูปเพื่อนับจำนวนคู่และจัดเรียงถุงเท้า
    for i in range(26):
        pairs = count[i] // 2  # หาจำนวนคู่
        if pairs > 0:
            result.extend([chr(i + ord('A')) * 2] * pairs)
            total_pairs += pairs
    
    # แสดงผลลัพธ์
    if result:
        print(" ".join(result))
    else:
        print("None")
    
    print(total_pairs)

main()