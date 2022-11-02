row_limit, col_limit = [int(x) for x in input().split(", ")]
decor_count, santa_row, santa_col, matrix, collected_items = 0, 0, 0, [], {"D": 0, "G": 0, "C": 0}


def move(srow, scol, direct, steps_):
    global row_limit, col_limit, collected_items, matrix, decor_count
    matrix[srow][scol] = "x"
    next_row, next_col = srow, scol
    options = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    for step in range(steps_):
        next_row, next_col = next_row + options[direct][0], next_col + options[direct][1]
        if direct == "up" and next_row < 0:
            next_row = row_limit - 1
        elif direct == "down" and next_row > row_limit - 1:
            next_row = 0
        elif direct == "left" and next_col < 0:
            next_col = col_limit - 1
        elif direct == "right" and next_col > col_limit - 1:
            next_col = 0

        if matrix[next_row][next_col] != "." and matrix[next_row][next_col] != "x":
            collected_items[matrix[next_row][next_col]] += 1
            decor_count -= 1
        if decor_count == 0:
            break
        matrix[next_row][next_col] = "x"
    return next_row, next_col


for row in range(row_limit):
    matrix.append(input().split())
    for _ in matrix[row]:
        if _ == "Y":
            santa_row, santa_col = row, matrix[row].index("Y")
        if _ != "." and _ != "Y":
            decor_count += 1

command_line = input()
while command_line != "End":
    direction, steps = [int(x) if x.isdigit() else x for x in command_line.split("-")]
    santa_row, santa_col = move(santa_row, santa_col, direction, steps)
    matrix[santa_row][santa_col] = "Y"
    if decor_count == 0:
        print("Merry Christmas!")
        break
    command_line = input()

print(f"You've collected:\n- {collected_items['D']} Christmas decorations\n- {collected_items['G']} Gifts\n- {collected_items['C']} Cookies")
[print(*r) for r in matrix]