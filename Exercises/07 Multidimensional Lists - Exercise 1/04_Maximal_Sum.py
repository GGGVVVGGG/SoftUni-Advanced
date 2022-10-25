r, c = [int(x) for x in input().split()]

matrix = []
for _ in range(r):
    matrix.append([int(x) for x in input().split()])

top_sum = []
for row in range(3):
    for col in range(3):
        top_sum.append(matrix[row][col])

current = []
for row in range(r - 2):
    for col in range(c - 2):
        current = [
            matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
            matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
            matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
        ]
        if sum(current) > sum(top_sum):
            top_sum = current
        else:
            current = []

print(f'Sum = {sum(top_sum)}')

while top_sum:
    current = top_sum[:3]
    top_sum = top_sum[3:]
    print(*current)