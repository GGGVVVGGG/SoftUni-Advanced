r, c = [int(x) for x in input().split(", ")]
matrix = [[int(el) for el in input().split(", ")] for row in range(r)]
print(sum([sum(x) for x in matrix]))
print(matrix)