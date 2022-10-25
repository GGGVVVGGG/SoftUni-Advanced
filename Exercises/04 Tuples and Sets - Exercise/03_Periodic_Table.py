n = int(input())
el = set()

for _ in range(n):
    [el.add(x) for x in input().split()]

print(*el, sep="\n")