matrix = [[int(x) for x in input().split(", ")] for x in range(int(input()))]
merged = []

for row in matrix:
    for el in row:
        merged.append(el)

print(merged)