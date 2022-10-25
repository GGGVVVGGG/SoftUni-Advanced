size = int(input())
matrix = [[int(x) for x in input().split(", ")] for x in range(size)]

p_nums = []
s_nums = []

for r in range(len(matrix)):
    p_nums.append(matrix[r][r])
    s_nums.append(matrix[r][size - 1 - r])

print(f'Primary diagonal: {", ".join(str(x) for x in p_nums)}. Sum: {sum(p_nums)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in s_nums)}. Sum: {sum(s_nums)}')