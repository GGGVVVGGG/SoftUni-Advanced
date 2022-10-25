size = int(input())
matrix = [[int(x) for x in input().split(" ")] for x in range(size)]

p_nums = []
s_nums = []

for r in range(len(matrix)):
    p_nums.append(matrix[r][r])
    s_nums.append(matrix[r][size - 1 - r])

print(f'{abs(sum(p_nums) - sum(s_nums))}')