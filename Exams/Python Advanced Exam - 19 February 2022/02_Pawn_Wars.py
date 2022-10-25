matrix = []
b_row, b_col, w_col, w_row = 0, 0, 0, 0

for row in range(8):
    matrix.append(input().split())
    if "w" in matrix[row]:
        w_row, w_col = row, matrix[row].index("w")
    elif "b" in matrix[row]:
        b_row, b_col = row, matrix[row].index("b")

while True:

    if (w_row - 1, w_col - 1) == (b_row, b_col) or (w_row - 1, w_col + 1) == (b_row, b_col):
        print(f"Game over! White win, capture on {chr(97 + b_col)}{abs(b_row - 8)}.")
        break
    w_row -= 1
    if w_row == -1:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + w_col)}8.")
        break

    if (b_row + 1, b_col - 1) == (w_row, w_col) or (b_row + 1, b_col + 1) == (w_row, w_col):
        print(f"Game over! Black win, capture on {chr(97 + w_col)}{abs(w_row - 8)}.")
        break
    b_row += 1
    if b_row == 8:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + b_col)}1.")
        break