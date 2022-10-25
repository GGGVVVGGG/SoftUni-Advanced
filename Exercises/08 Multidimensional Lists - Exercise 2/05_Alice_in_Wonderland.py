def move_next(row, col, t_row, t_col, directions, current_direction):
    global outside
    global dead
    global collected_tea
    global final_msg
    new_row, new_col = row + directions[current_direction][0], col + directions[current_direction][1]
    if new_row == t_row and new_col == t_col:
        matrix[new_row][new_col] = "*"
        dead = True
        final_msg = "Alice didn't make it to the tea party."
        return new_col, new_col
    if 0 > new_row or 0 > new_col or new_row > SIZE -1 or new_col > SIZE -1:
        final_msg = "Alice didn't make it to the tea party."
        outside = True
        return new_row, new_col
    if type(matrix[new_row][new_col]) == int:
        collected_tea += matrix[new_row][new_col]
        return new_row, new_col
    return new_row, new_col


SIZE = int(input())
matrix = []
alice_row = 0
alice_col = 0
trap_row = 0
trap_col = 0
collected_tea = 0
outside = False
dead = False
final_msg = "She did it! She went to the party."

for row in range(SIZE):
    matrix.append([int(x) if x.lstrip("").isdigit() else x for x in input().split()])
    for col, ch in enumerate(matrix[row]):
        if ch == "A":
            alice_row = row
            alice_col = col
        elif ch == "R":
            trap_row = row
            trap_col = col

directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, +1]}

while True:
    matrix[alice_row][alice_col] = "*"
    if collected_tea >= 10:
        break
    current_move = input()
    alice_row, alice_col = move_next(alice_row, alice_col, trap_row, trap_col, directions, current_move)
    if dead:
        break
    if outside:
        break

print(final_msg)
for row in range(len(matrix)):
    print(*matrix[row], sep=" ")
