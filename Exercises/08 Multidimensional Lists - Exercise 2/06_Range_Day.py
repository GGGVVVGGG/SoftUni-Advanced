def get_next_pos(r, c, d, s=1):
    moves = {
        "up": [r - s, c],
        "down": [r + s, c],
        "left": [r, c - s],
        "right": [r, c + s]
    }
    return moves[d][0], moves[d][1]


def is_valid(r, c, s):
    return 0 <= r < s and 0 <= c < s


size = 5
player_r = 0
player_c = 0
total_targets = 0
shot_targets = []

matrix = []
for row in range(5):
    row_input = input().split()
    matrix.append(row_input)
    for col in range(size):
        if row_input[col] == "x":
            total_targets += 1
        elif row_input[col] == "A":
            player_r = row
            player_c = col

left_targets = total_targets

cmd_n = int(input())
for _ in range(cmd_n):

    command_args = input().split()
    command = command_args[0]
    direction = command_args[1]

    if command == "move":

        step = int(command_args[2])
        next_row, next_col = get_next_pos(player_r, player_c, direction, step)

        if is_valid(next_row, next_col, size) and matrix[next_row][next_col] == ".":
            matrix[player_r][player_c] = "."
            player_r, player_c = next_row, next_col
            matrix[player_r][player_c] = "A"
    else:

        bullet_r, bullet_c = get_next_pos(player_r, player_c, direction)
        while is_valid(bullet_r, bullet_c, size):
            if matrix[bullet_r][bullet_c] == "x":
                left_targets -= 1
                shot_targets.append([bullet_r, bullet_c])
                matrix[bullet_r][bullet_c] = "."
                break
            bullet_r, bullet_c = get_next_pos(bullet_r, bullet_c, direction)

    if left_targets == 0:
        break

print(f"Training completed! All {total_targets} targets hit." if left_targets == 0 else f"Training not completed! {left_targets} targets left.")

for target in shot_targets:
    print(target)