magic_number = int(input())
matrix = [[int(x) for x in input().split()] for x in range(magic_number)]

result = 0
for n in range(magic_number):
    result += matrix[n][n]

print(result)