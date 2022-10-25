def valid(rol, col, size):
    return 0 <= rol < size and 0 <= col < size


def is_knight(rol, col, matrix):
    return matrix[rol][col] == "K"


def check_hit(row, col):
    current_hits = 0
    if valid(row - 2, col - 1, size) and is_knight(row - 2, col - 1, matrix):
        current_hits += 1
    if valid(row - 2, col + 1, size) and is_knight(row - 2, col + 1, matrix):
        current_hits += 1
    if valid(row + 2, col + 1, size) and is_knight(row + 2, col + 1, matrix):
        current_hits += 1
    if valid(row + 2, col - 1, size) and is_knight(row + 2, col - 1, matrix):
        current_hits += 1
    if valid(row - 1, col - 2, size) and is_knight(row - 1, col - 2, matrix):
        current_hits += 1
    if valid(row + 1, col - 2, size) and is_knight(row + 1, col - 2, matrix):
        current_hits += 1
    if valid(row + 1, col + 2, size) and is_knight(row + 1, col + 2, matrix):
        current_hits += 1
    if valid(row - 1, col + 2, size) and is_knight(row - 1, col + 2, matrix):
        current_hits += 1
    return current_hits


size = int(input())
matrix = []
all_knights = {}
knights_removed = 0

for row in range(size):
    matrix.append(list(input()))
    for col in range(len(matrix[row])):
        if is_knight(row, col, matrix):
            all_knights[f"{row} {col}"] = 0

while all_knights:
    max_hits = 0
    max_knight = None
    for knight, hits in all_knights.items():
        k_row, k_col = [int(x) for x in knight.split()]
        all_knights[knight] = check_hit(k_row, k_col)
    for knight, value in all_knights.items():
        if value > max_hits:
            max_hits = value
            max_knight = knight
    if max_knight:
        m_row, m_col = [int(x) for x in max_knight.split()]
        matrix[m_row][m_col] = "0"
        del all_knights[max_knight]
        knights_removed += 1
    to_delete = []
    for knight, value in all_knights.items():
        if value == 0:
            to_delete.append(knight)
    for item in to_delete:
        del all_knights[item]


print(knights_removed)
# [print(*row) for row in matrix]