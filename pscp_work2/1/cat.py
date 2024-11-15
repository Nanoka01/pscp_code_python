def cat_parade():
    cat_dict = {}  # เก็บจำนวนแมวและตำแหน่งที่เจอครั้งแรก
    cat_list = []  # เก็บลำดับของแมวที่เจอในพาเหรด
    position = 0   # ลำดับที่เจอแมวในพาเหรด

    while True:
        line = input()
        if line == "END":
            break
        elif line == "IT'S A DOG":
            # ลบแมวตัวล่าสุดออก
            if cat_list:
                last_cat = cat_list.pop()
                cat_dict[last_cat]['count'] -= 1
                if cat_dict[last_cat]['count'] == 0:
                    del cat_dict[last_cat]
        else:
            # แยกสายพันธุ์แมวตาม ", " และจัดเก็บ
            cats = line.split(", ")
            for cat in cats:
                position += 1  # เพิ่มตำแหน่งเมื่อเจอแมวใหม่
                if cat not in cat_dict:
                    cat_dict[cat] = {'first_position': position, 'count': 0}
                cat_dict[cat]['count'] += 1
                cat_list.append(cat)

    # แสดงผลลัพธ์เรียงตามชื่อแมวตามพจนานุกรม
    for cat in sorted(cat_dict.keys()):
        print(f"{cat} {cat_dict[cat]['first_position']} {cat_dict[cat]['count']}")

# เรียกใช้ฟังก์ชัน
cat_parade()
