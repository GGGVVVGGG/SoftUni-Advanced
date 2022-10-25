n = int(input())
odd = set()
even = set()

for row in range(1, n + 1):
    name = input()
    r = 0
    for ch in name:
        r += ord(ch)
    r //= row
    if r % 2 == 0:
        even.add(r)
    else:
        odd.add(r)

if sum(odd) == sum(even):
    print(', '.join([str(x) for x in odd.union(even)]))
elif sum(odd) > sum(even):
    print(', '.join([str(x) for x in odd.difference(even)]))
elif sum(odd) < sum(even):
    print(', '.join([str(x) for x in odd.symmetric_difference(even)]))