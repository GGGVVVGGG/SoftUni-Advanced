from collections import  deque
food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))
for _ in range(len(orders)):
    if orders[0] <= food:
        food -= orders[0]
        orders.popleft()
    else:
        break

if not orders:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")