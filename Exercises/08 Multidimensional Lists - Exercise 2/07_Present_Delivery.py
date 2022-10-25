def get_next_position(direction, s_row, s_col):
    move = {"up": [-1, 0], "down": [+1, 0], "left": [0, -1], "right": [0, +1]}
    return s_row + move[direction][0], s_col + move[direction][1]


def cookie(s_row, s_col):
    global plot, presents_cnt, good_kids_with_gifts
    directions = [[-1, 0], [+1, 0], [0, -1], [0, +1]]
    for direction in directions:
        if plot[s_row + direction[0]][s_col + direction[1]] != "-":
            if plot[s_row + direction[0]][s_col + direction[1]] == "V":
                good_kids_with_gifts -= 1
                presents_cnt -= 1
            else:
                presents_cnt -= 1
            plot[s_row + direction[0]][s_col + direction[1]] = "-"


presents_cnt = int(input())
plot_size = int(input())

# kids
good_kids = 0

# santa
santa_row = 0
santa_col = 0

plot = []
for row in range(plot_size):
    this_row = input().split()
    plot.append(this_row)
    for col, ch in enumerate(this_row):
        if ch == "S":
            santa_row, santa_col = row, col
        elif ch == "V":
            good_kids += 1

good_kids_with_gifts = good_kids

command = input()
while command != "Christmas morning":
    plot[santa_row][santa_col] = "-"
    santa_row, santa_col = get_next_position(command, santa_row, santa_col)
    if plot[santa_row][santa_col] == "V":
        good_kids_with_gifts -= 1
        presents_cnt -= 1
        # print("Good kid")
    elif plot[santa_row][santa_col] == "C":
        cookie(santa_row,santa_col)
        # print("Cookie")
    plot[santa_row][santa_col] = "S"
    # [print(row) for row in plot]
    # print()
    if presents_cnt <= 0:
        if good_kids_with_gifts > 0:
            print("Santa ran out of presents!")
        break
    command = input()

[print(*row) for row in plot]
print(f"Good job, Santa! {good_kids} happy nice kid/s." if presents_cnt >= good_kids_with_gifts == 0 else f"No presents for {good_kids_with_gifts} nice kid/s.")
