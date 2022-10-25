from collections import deque

name = input()
tail = deque()

while name != "End":
    if name == "Paid":
        while tail:
            print(tail.popleft())
    else:
        tail.append(name)
    name = input()

print(f"{len(tail)} people remaining.")