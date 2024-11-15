def main():
    """Check if each number is a Harshad Number"""
    total = []
    
    for _ in range(10):
        while True:  # วนรับอินพุตจนกว่าจะได้รับข้อมูลที่ถูกต้อง
            try:
                number = int(input("Enter a number: "))
                break  # หากป้อนตัวเลขได้ถูกต้อง ให้ออกจากลูป
            except ValueError:
                print("Invalid input. Please enter a valid integer.")  # แจ้งเตือนเมื่ออินพุตไม่ถูกต้อง
        digit_sum = sum(int(digit) for digit in str(number))
        
        if number % digit_sum == 0:
            total.append("Yes")
        else:
            total.append("No")
    for result in total:
        print(result)

main()
