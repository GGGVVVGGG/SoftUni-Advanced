def invalid_command(row, col):
    return 0 > row or row > size - 1 or 0 > col or col > size - 1


size = int(input())
commands = input().split()

coal_total = 0
miner_position = []
exit_position = []
exitt = False

matrix = []

for row in range(size):
    matrix.append(input().split())
    if "c" in matrix[row]:
        coal_total += matrix[row].count("c")
    if "e" in matrix[row]:
        exit_position = [row, matrix[row].index("e")]
    if "s" in matrix[row]:
        miner_position = [row, matrix[row].index("s")]

current_position = miner_position

for command in commands:
    if command == "up":
        if invalid_command(current_position[0] - 1, current_position[1]):
            continue
        if matrix[current_position[0] - 1][current_position[1]] == "c":
            matrix[current_position[0] - 1][current_position[1]] = "*"
            current_position = [current_position[0] - 1, current_position[1]]
            coal_total -= 1
            if coal_total == 0:
                break
        elif matrix[current_position[0] - 1][current_position[1]] == "e":
            current_position = [current_position[0] - 1, current_position[1]]
            exitt = True
            break
        else:
            current_position = [current_position[0] - 1, current_position[1]]

    elif command == "down":
        if invalid_command(current_position[0] + 1, current_position[1]):
            continue
        if matrix[current_position[0] + 1][current_position[1]] == "c":
            matrix[current_position[0] + 1][current_position[1]] = "*"
            current_position = [current_position[0] + 1, current_position[1]]
            coal_total -= 1
            if coal_total == 0:
                break
        elif matrix[current_position[0] + 1][current_position[1]] == "e":
            current_position = [current_position[0] + 1, current_position[1]]
            exitt = True
            break
        else:
            current_position = [current_position[0] + 1, current_position[1]]

    elif command == "left":
        if invalid_command(current_position[0], current_position[1] - 1):
            continue
        if matrix[current_position[0]][current_position[1] - 1] == "c":
            matrix[current_position[0]][current_position[1] - 1] = "*"
            current_position = [current_position[0], current_position[1] - 1]
            coal_total -= 1
            if coal_total == 0:
                break
        elif matrix[current_position[0]][current_position[1] - 1] == "e":
            current_position = [current_position[0], current_position[1] - 1]
            exitt = True
            break
        else:
            current_position = [current_position[0], current_position[1] - 1]

    elif command == "right":
        if invalid_command(current_position[0], current_position[1] + 1):
            continue
        if matrix[current_position[0]][current_position[1] + 1] == "c":
            matrix[current_position[0]][current_position[1] + 1] = "*"
            current_position = [current_position[0], current_position[1] + 1]
            coal_total -= 1
            if coal_total == 0:
                break
        elif matrix[current_position[0]][current_position[1] + 1] == "e":
            current_position = [current_position[0], current_position[1] + 1]
            exitt = True
            break
        else:
            current_position = [current_position[0], current_position[1] + 1]

# print()
# for row in matrix:
#     print(row)
# print()
# print("commands list:", commands)
# print("total coal:", coal_total)
# print("exit state:", exitt)
# print("exit position:", exit_position)
# print("miner position:", miner_position)
# print("current position:", current_position)

if coal_total == 0:
    print(f"You collected all coal! ({current_position[0]}, {current_position[1]})")
elif coal_total > 0 and exitt:
    print(f"Game over! ({current_position[0]}, {current_position[1]})")
else:
    print(f"{coal_total} pieces of coal left. ({current_position[0]}, {current_position[1]})")
