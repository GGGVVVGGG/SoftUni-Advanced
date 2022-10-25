rows, columns = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split()] for x in range(rows)]

for col in range(columns):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][col]
    print(current_sum)