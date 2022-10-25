from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
operators = deque(x for x in input().split())
honey = 0

while bees and nectar:
    bee = bees[0]
    c_nectar = nectar.pop()
    if c_nectar < bee:
        continue
    else:
        operator = operators.popleft()
        if operator == "+":
            honey += bee + c_nectar
        elif operator == "-":
            honey += abs(bee - c_nectar)
        elif operator == "*":
            honey += bee * c_nectar
        elif operator == "/" and c_nectar > 0:
            honey += abs(bee / c_nectar)
        bees.popleft()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
elif nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")