player1, player2 = input().split(", ")
matrix = [input().split() for x in range(6)]
p1_rest = False
p2_rest = False

while True:
    p1_row, p1_col = [int(x) for x in input().lstrip("(").rstrip(")").split(", ")]
    if not p1_rest:
        if matrix[p1_row][p1_col] == "W":
            print(f"{player1} hits a wall and needs to rest.")
            p1_rest = True
        if matrix[p1_row][p1_col] == "T":
            print(f"{player1} is out of the game! The winner is {player2}.")
            break
        if matrix[p1_row][p1_col] == "E":
            print(f"{player1} found the Exit and wins the game!")
            break
    else:
        p1_rest = False
    p2_row, p2_col = [int(x) for x in input().lstrip("(").rstrip(")").split(", ")]
    if not p2_rest:
        if matrix[p2_row][p2_col] == "W":
            print(f"{player2} hits a wall and needs to rest.")
            p2_rest = True
        if matrix[p2_row][p2_col] == "T":
            print(f"{player2} is out of the game! The winner is {player1}.")
            break
        if matrix[p2_row][p2_col] == "E":
            print(f"{player2} found the Exit and wins the game!")
            break
    else:
        p2_rest = False