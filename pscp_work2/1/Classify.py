"""Classify"""
def main():
    """Classify"""
    data = []
    while True:
        student_id = input()
        if student_id == "END":
            break
        year = student_id[:2]
        faculty = student_id[2:4]
        data.append((year, int(faculty)))
    data.sort()
    data_dict = {}
    for year,faculty in data:
        if f"{year} {faculty}" in data_dict:
            data_dict[f"{year} {faculty}"] = data_dict[f"{year} {faculty}"]+1
        else:
            data_dict[f"{year} {faculty}"] = 1
    key_dict = {}
    for key,value in data_dict.items():
        if key[:2] in key_dict:
            print(f"--{key[2:]} {value}")
        else:
            print(f"{key} {value}")
            key_dict[key[:2]] = value
main()

"""
คุณจะได้รับข้อมูลนักศึกษาเป็นจำนวนมาก

มากจนกว่าจะได้รับข้อความว่า END



ข้อมูลของนักศึกษาประกอบด้วย

รหัสนักศึกษา



ให้แสดงผลแยกชั้นปี และแยกคณะ

แยกชั้นปีให้แสดงผลจากปีที่สูงที่สุด(แก่) และแสดงผลคณะตามรหัสคณะ และบอกจำนวนคน

รูปแบบให้ดูจาก Sample Output น่าจะเข้าใจง่ายกว่า

 

Input Specification
หลายบรรทัดตามที่บอก

ปิดบรรทัดสุดท้ายด้วย END เสมอ

 

Output Specification
มีได้หลายบรรทัด
"""