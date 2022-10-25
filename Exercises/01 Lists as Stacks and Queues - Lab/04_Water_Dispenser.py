from collections import deque

water = int(input())

people = deque()

person = input()
while person != "Start":
    people.append(person)
    person = input()

command = input()
while command != "End":
    command = command.split()
    if len(command) == 1:
        wanted = int(command[0])
        if wanted <= water:
            print(f"{people[0]} got water")
            water -= wanted
            people.popleft()
        else:
            print(f"{people[0]} must wait")
            people.popleft()
    elif len(command) == 2:
        addon = int(command[1])
        water += addon

    command = input()

print(f"{water} liters left")