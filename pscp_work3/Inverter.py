def binary_inverter(binary_str):
    # Step 2: Invert bits
    inverted_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)
    
    # Step 3: Remove leading zeros
    inverted_str = inverted_str.lstrip('0')
    
    # If the result is empty after stripping, that means it's all zeros, so return '0'
    if inverted_str == '':
        return '0'
    
    return inverted_str

# รับค่า input เป็นฐานสอง
binary_input = input()

# แสดงผลลัพธ์หลังจาก Invert แล้ว
print(binary_inverter(binary_input))
