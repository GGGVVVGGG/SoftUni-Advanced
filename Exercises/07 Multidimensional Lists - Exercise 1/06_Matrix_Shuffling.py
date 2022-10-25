dimensions = input().split()
matrix_rows, matrix_columns = [int(x) for x in dimensions]

matrix = []
for row in range(matrix_rows):
    matrix.append(input().split())

while True:
    command = input().split()
    if command[0] == "END":
        break

    if len(command) != 5 or command[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if row1 < 0 or row2 < 0 or col1 < 0 or col2 < 0 or row1 >= matrix_rows or row2 >= matrix_rows or col1 >= matrix_columns or col2 >= matrix_columns:
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row in matrix:
        print(*row, sep=" ")