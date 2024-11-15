"""=PrasomSib"""
def main():
    """หาผลรวมให้ได้สิบจากตัวเลขที่อยู่ติดกัน"""
    numbers = input().strip()  # รับ input และลบช่องว่างหรือ newline ท้ายข้อความ
    count = 0

    # วนลูปหากลุ่มของตัวเลขตั้งแต่สองหลักขึ้นไป
    for i in range(len(numbers)):
        current_sum = 0
        # ลูปตรวจสอบกลุ่มของตัวเลขที่ต่อกัน
        for j in range(i, len(numbers)):
            current_sum += int(numbers[j])
            if current_sum == 10:  # หากผลรวมเป็น 10
                count += 1
            elif current_sum > 10:  # ถ้าผลรวมเกิน 10 ก็ไม่ต้องตรวจสอบต่อ
                break

    print(count)  # แสดงจำนวนวิธีที่สามารถรวมได้ 10

main()
