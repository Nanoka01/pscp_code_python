def check_winner(board):
    # ตรวจสอบแถวและหลัก
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            return board[i][0] + " WIN"
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            return board[0][i] + " WIN"
    
    # ตรวจสอบเส้นทแยงมุม
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0] + " WIN"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2] + " WIN"
    
    # ตรวจสอบว่าเป็น DRAW หรือไม่
    for row in board:
        if '-' in row:
            return "DRAW"
    
    return "DRAW"

# รับข้อมูลของกระดาน OX
board = []
for i in range(3):
    row = input().strip()
    board.append(row)

# ตรวจสอบและแสดงผลลัพธ์
result = check_winner(board)
print(result)


