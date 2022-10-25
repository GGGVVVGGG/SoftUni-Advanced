def move(dir_, urow, ucol):
    dir__ = {"up": [-1, 0, 5], "down": [1, 0, 5], "left": [0, -1, 5], "right": [0, 1, 5]}
    if dir_ == "up":
        if urow == 0:
            return urow + dir__[dir_][2], ucol
        return urow + dir__[dir_][0], ucol
    elif dir_ == "down":
        if urow == 5:
            return urow - dir__[dir_][2], ucol
        return urow + dir__[dir_][0], ucol
    elif dir_ == "left":
        if ucol == 0:
            return urow, ucol + dir__[dir_][2]
        return urow, ucol + dir__[dir_][1]
    elif dir_ == "right":
        if ucol == 5:
            return urow, ucol - dir__[dir_][2]
        return urow, ucol + dir__[dir_][1]


elements = ["W", "M", "C"]
element_names = {"W": "Water", "M": "Metal", "C": "Concrete"}
rover_row, rover_col = 0, 0

matrix = [input().split() for _ in range(6)]
for rr in range(6):
    for rc in range(6):
        if matrix[rr][rc] == "E":
            rover_row, rover_col = rr, rc

commands = input().split(", ")
for i in range(len(commands)):
    command = commands[i]
    rover_row, rover_col = move(command, rover_row, rover_col)
    target = matrix[rover_row][rover_col]
    if target == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break
    if target != "-":
        print(f"{element_names[target]} deposit found at ({rover_row}, {rover_col})")
        if target in elements:
            elements.pop(elements.index(target))

if not elements:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")