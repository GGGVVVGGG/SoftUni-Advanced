from collections import deque

dd = deque()
cnt = int(input())
for _ in range(cnt):
    command = input().split()
    if len(command) == 2:
        nbr = int(command[1])
        dd.append(nbr)
    elif len(command) == 1:
        command = command[0]
        if command == "2" and dd:
            dd.pop()
        elif command == "3" and dd:
            print(max(dd))
        elif command == "4" and dd:
            print(min(dd))

for _ in range(len(dd)):
    if len(dd) > 1:
        print(dd.pop(), end=", ")
    else:
        print(dd.pop())