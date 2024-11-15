def main():
    crew = {}
    dead = {}

    # รับชื่อและบทบาทของสมาชิกจนกว่าจะเจอคำว่า 'Start'
    while True:
        inp = input()
        if inp == "Start":
            break
        inp = inp.strip('{}')  # ลบ {} ออกจาก input
        name, role = inp.split(" : ")
        crew[name] = role

    # รับชื่อผู้ที่ถูกโหวตให้ออกไปจนกว่าจะเจอคำว่า 'End'
    while True:
        inp = input()
        if inp == "End":
            break
        if inp in crew:
            dead[inp] = crew.pop(inp)

    # คำนวณจำนวน Impostor ที่เหลือ
    impostor_remains = list(crew.values()).count("Impostor")
    
    # แสดงจำนวน Impostor ที่เหลืออยู่
    print(f"{impostor_remains} Impostor Remains")

    # แสดงผู้รอดชีวิต (Alive)
    print("***Alive***")
    for name in sorted(crew):
        print(f"{name} : {crew[name]}")

    # แสดงผู้ที่เสียชีวิต (Dead)
    print("***Dead***")
    for name in sorted(dead):
        print(f"{name} : {dead[name]}")

main()

