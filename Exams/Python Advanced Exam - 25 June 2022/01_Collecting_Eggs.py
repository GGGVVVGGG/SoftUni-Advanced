from collections import deque

eggs = deque(int(x) for x in input().split(", "))
paper = deque(int(x) for x in input().split(", "))
boxes = 0

while eggs and paper:
    this_egg = eggs.popleft()
    if this_egg <= 0:
        continue
    if this_egg == 13:
        first_paper = paper.popleft()
        last_paper = paper.pop()
        paper.appendleft(last_paper)
        paper.append(first_paper)
        continue
    this_paper = paper.pop()
    if this_egg + this_paper <= 50:
        boxes += 1

print(f"Great! You filled {boxes} boxes." if boxes else "Sorry! You couldn't fill any boxes!")

if eggs:
    print("Eggs left:", ", ".join(str(x) for x in eggs))
if paper:
    print("Pieces of paper left:", ", ".join(str(x) for x in paper))
