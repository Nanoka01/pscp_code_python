"""BreachTheDoor"""
def main(text = input()):
    """BreachTheDoor"""
    punctuation = '''~`!@#$%&^*()-_+=}{[\\]|/:;'"<>,.?1234567890'''
    for i in punctuation:
        text = text.replace(i,"")
    new_text = text.split()
    result = []
    for i in new_text:
        if len(i) > 6:
            result.append(i)
    for _,i in enumerate(result):
        print(i,end=" ")
main()
"""
Input Specification
หนึ่งบรรทัด เป็นประโยคที่มีความยาวระดับหนึ่ง

Output Specification
หนึ่งบรรทัด คำที่มีความยาวมากกว่า 6 ตัวอักษร เรียงจากต้น Paragraph ไปจนสุด Paragraph
"""