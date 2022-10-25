def sub_matrix_ckeck_sum(matrix, row_index, column_index, submatrix_size):
    result = 0
    for r in range(row_index, row_index + submatrix_size):
        for c in range(column_index, column_index + submatrix_size):
            result += matrix[r][c]
    return result


def winning_matrix(matrix, best_row, best_column, submatrix_size):
    current = []
    for r in range(best_row, best_row + submatrix_size):
        for c in range(best_column, best_column + submatrix_size):
            current.append(matrix[r][c])
    return current


rows_cnt, columns_cnt = [int(x) for x in input().split(",")]
matrix = [[int(x) for x in input().split(", ")] for x in range(rows_cnt)]

submatrix_size = 2
top_sum = sub_matrix_ckeck_sum(matrix, 0, 0, submatrix_size)
top_row_index = 0
top_col_index = 0

for row in range(rows_cnt - submatrix_size + 1):
    for col in range(columns_cnt - submatrix_size + 1):
        current = sub_matrix_ckeck_sum(matrix, row, col, submatrix_size)
        if current > top_sum:
            top_sum = current
            top_row_index = row
            top_col_index = col

winner = winning_matrix(matrix, top_row_index, top_col_index, submatrix_size)
for index in range(0, len(winner), 2):
    print(f'{winner[index]} {winner[index + 1]}')
print(top_sum)