from collections import deque

chock = [int(g) for g in input().split(", ")]
cum = deque([int(g) for g in input().split(", ")])
shakes = 0
while chock and cum and shakes < 5:
    curr_chock = chock.pop()
    curr_cum = cum.popleft()

    if curr_chock <= 0 and curr_cum <= 0:
        continue

    if curr_chock <= 0:
        cum.appendleft(curr_cum)
        continue

    if curr_cum <= 0:
        chock.append(curr_chock)
        continue

    if curr_chock == curr_cum:
        shakes += 1
        continue

    else:
        cum.append(curr_cum)
        chock.append(curr_chock - 5)

print("Great! You made all the chocolate milkshakes needed!" if shakes == 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join([str(x) for x in chock])}" if chock else "Chocolate: empty")
print(f"Milk: {', '.join(str(x) for x in cum)}" if cum else "Milk: empty")