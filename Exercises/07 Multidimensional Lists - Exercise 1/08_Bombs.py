def get_neighbours(row, col, matrix):
    size = len(matrix)
    neigbours = []
    if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
        neigbours.append([row - 1, col])
    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neigbours.append([row + 1, col])
    if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
        neigbours.append([row, col - 1])
    if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
        neigbours.append([row, col + 1])
    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neigbours.append([row + 1, col - 1])
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neigbours.append([row + 1, col + 1])
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neigbours.append([row - 1, col - 1])
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neigbours.append([row - 1, col + 1])
    return neigbours


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


r_c = int(input())
matrix = []
for _ in range(r_c):
    matrix.append([int(x) for x in input().split()])

bombs = [x.split(",") for x in input().split()]
# print(bombs)

for bomb in bombs:
    bomb_row, bomb_col = int(bomb[0]), int(bomb[1])
    # print(bomb_row,bomb_col)
    if matrix[bomb_row][bomb_col] <= 0:
        continue
    bomb_power = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0
    neighbours = get_neighbours(bomb_row, bomb_col, matrix)
    for neighbour in neighbours:
        n_row = neighbour[0]
        n_col = neighbour[1]
        matrix[n_row][n_col] -= bomb_power

live_cells = []
for row in matrix:
    for el in row:
        if el > 0:
            live_cells.append(el)

print(f"Alive cells: {len(live_cells)}")
print(f"Sum: {sum(live_cells)}")

for row in matrix:
    print(f"{' '.join(str(x) for x in row)}")