def find_day(d, m):
    """หาวันที่ตรงกับวันที่ d เดือน m ของปี 2011"""
    # จำนวนวันในแต่ละเดือน
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # ชื่อวันในแต่ละลำดับ
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # คำนวณจำนวนวันจากวันที่ 1 มกราคม 2011 ถึงวันที่ d ของเดือน m
    total_days = sum(days_in_month[:m-1]) + d - 1

    # หาวันที่ตรงกันจากการนับจำนวนวันทั้งหมด % 7
    return days_of_week[total_days % 7]

# รับค่า input
d = int(input())
m = int(input())

# แสดงผลลัพธ์
print(find_day(d, m))
