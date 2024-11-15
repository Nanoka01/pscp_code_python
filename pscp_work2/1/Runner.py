"""Runner"""
def main():
    """Runner"""
    distance = int(input())
    result = []
    data = []
    for i in range(1, int(input())+1):
        x, y = map(int, input().split())
        data.append((x, distance-y, i))
    sort_data = sorted(data, key = lambda x: (x[1]/x[0], -x[0]))
    for x, _, i in sort_data:
        result.append(i)
    print(result[0])
main()
"""
Input Specification
บรรทัดแรก : เป็นระยะทางวิ่งรวม d วัดจากจุดเริ่มต้น [ 1 <= d <= 2**30 ] หน่วยเป็นเมตร

บรรทัดที่สอง : เป็นจำนวนผู้เข้าแข่งขัน n [ 1 <= n <= 8191]

อีก n บรรทัดต่อมา : จะเป็นข้อมูลของหมายเลขนักวิ่งคนที่ 1 ถึงคนที่ n เรียงตามลำดับไป
         โดยในแต่ละบรรทัดจะมีตัวเลข 2 จำนวน แบ่งด้วยช่องว่าง 1 ช่อง  

         จำนวนแรกจะเป็นความเร็วของนักวิ่งคนที่ i
         (เป็นจำนวนเต็ม หน่วย เมตรต่อวินาที)  

         จำนวนที่สองเป็นจุดเริ่มต้นที่นักวิ่งเริ่มต้นคนที่ i วัดจากเป็นระยะห่างจากจุดเริ่มต้น
         (เป็นจำนวนเต็ม หน่วย เมตร)

         i เป็นหมายเลขนักวิ่ง, 1 <= i <= n

 

Output Specification
หนึ่งบรรทัดเท่านั้น คือหมายเลขของนักวิ่งที่ชนะในการแข่งขันครั้งนี้
"""