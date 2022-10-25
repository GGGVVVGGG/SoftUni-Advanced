from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pumps.append([int(g) for g in input().split()])

for attempt in range(n):
    tank = 0
    failed = False
    for petrol, distance in pumps:
        tank += petrol
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
