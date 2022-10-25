def move(dire, row, col):
    option = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
    return row + option[dire][0], col + option[dire][1]


SIZE = 6
matrix = []
for _ in range(SIZE):
    matrix.append(input().split())

my_row, my_col = [int(x) for x in input().strip("(").strip(")").split(", ")]

command_line = input()
while command_line != "Stop":
    command_line = command_line.split(", ")
    command = command_line[0]
    direction = command_line[1]
    if command != "Read" and command != "Delete":
        value = command_line[2]

    new_row, new_col = move(direction, my_row, my_col)
    if command == "Create":
        if matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = value
    elif command == "Update":
        if matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = value
    elif command == "Delete":
        matrix[new_row][new_col] = "."
    elif command == "Read":
        if matrix[new_row][new_col] != ".":
            print(matrix[new_row][new_col])

    my_row, my_col = new_row, new_col
    command_line = input()

[print(*row) for row in matrix]