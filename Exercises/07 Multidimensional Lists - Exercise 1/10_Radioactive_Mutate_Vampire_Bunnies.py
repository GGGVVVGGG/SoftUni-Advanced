mtrx_rows, mtrx_cols = [int(x) for x in input().split()]
matrix = []
bombs = set()
player_row = 0
player_col = 0
win = False
dead = False

for row in range(mtrx_rows):
    current_row = []
    line = input()
    for idx, ch in enumerate(line):
        if ch == "B":
            bombs.add(f"{row} {idx}")
        elif ch == "P":
            player_row = row
            player_col = idx
        current_row.append(ch)
    matrix.append(current_row)


def get_next(player_row, player_col, command):
    if command == "U":
        return player_row - 1, player_col
    elif command == "D":
        return player_row + 1, player_col
    elif command == "L":
        return player_row, player_col - 1
    elif command == "R":
        return player_row, player_col + 1


def is_outside(new_row, new_col, rows, cols):
    return new_row < 0 or new_col < 0 or new_row >= rows or new_col >= cols


commands = input()
matrix[player_row][player_col] = "."
for command in commands:
    next_row, next_col = get_next(player_row, player_col, command)
    if is_outside(next_row, next_col, mtrx_rows, mtrx_cols):
        win = True
    elif matrix[next_row][next_col] == "B":
        dead = True
        player_row, player_col = next_row, next_col
    else:
        player_row, player_col = next_row, next_col

    new_bombs = set()
    for bomb in bombs:
        bomb_row, bomb_col = [int(x) for x in bomb.split()]
        if not is_outside(bomb_row - 1, bomb_col, mtrx_rows, mtrx_cols):
            matrix[bomb_row - 1][bomb_col] = "B"
            new_bombs.add(f"{bomb_row - 1} {bomb_col}")
        if not is_outside(bomb_row + 1, bomb_col, mtrx_rows, mtrx_cols):
            matrix[bomb_row + 1][bomb_col] = "B"
            new_bombs.add(f"{bomb_row + 1} {bomb_col}")
        if not is_outside(bomb_row, bomb_col - 1, mtrx_rows, mtrx_cols):
            matrix[bomb_row][bomb_col - 1] = "B"
            new_bombs.add(f"{bomb_row} {bomb_col - 1}")
        if not is_outside(bomb_row, bomb_col + 1, mtrx_rows, mtrx_cols):
            matrix[bomb_row][bomb_col + 1] = "B"
            new_bombs.add(f"{bomb_row} {bomb_col + 1}")
        bombs = bombs | new_bombs
    if matrix[player_row][player_col] == "B":
        dead = True
    if win or dead:
        break

[print(*row, sep="") for row in matrix]
if win:
    print("won:", player_row, player_col)
else:
    print("dead:", player_row, player_col)