from collections import deque

kids = deque(input().split())
cnt = int(input()) - 1
while len(kids) > 1:
    for _ in range(cnt):
        current = kids.popleft()
        kids.append(current)
    print(f"Removed {kids[0]}")
    kids.popleft()

print(f"Last is {kids[0]}")
