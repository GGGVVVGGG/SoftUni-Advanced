def collect_in_direction(b_row, b_col, direction):
    current_collection = []
    if direction == "up":
        while 1 <= b_row:
            b_row -= 1
            if matrix[b_row][b_col] == "X":
                return current_collection
            current_collection.append([b_row, b_col])
        return current_collection
    elif direction == "down":
        while b_row < SIZE - 1:
            b_row += 1
            if matrix[b_row][b_col] == "X":
                return current_collection
            current_collection.append([b_row, b_col])
        return current_collection
    elif direction == "left":
        while 1 <= b_col:
            b_col -= 1
            if matrix[b_row][b_col] == "X":
                return current_collection
            current_collection.append([b_row, b_col])
        return current_collection
    elif direction == "right":
        while b_col < SIZE - 1:
            b_col += 1
            if matrix[b_row][b_col] == "X":
                return current_collection
            current_collection.append([b_row, b_col])
        return current_collection


def get_largest_sum(collected):
    largest = float('-Inf')
    largest_sum_dict = {}
    for direction, collected_coordinates in collected.items():
        current_sum = 0
        if not collected_coordinates:
            continue
        for this in collected_coordinates:
            current_sum += matrix[this[0]][this[1]]
        if current_sum > largest:
            largest = current_sum
            largest_sum_dict = {direction: collected_coordinates}
    return largest, largest_sum_dict


SIZE = int(input())
moves = ["up", "down", "left", "right"]
matrix = []
collections = {}
bunny_row = 0
bunny_col = 0


for row in range(SIZE):
    matrix.append([int(x) if x != "X" and x != "B" else x for x in input().split()])
    for col in range(len(matrix[row])):
        if matrix[row][col] == "B":
            bunny_row = row
            bunny_col = col


for move in moves:
    if collect_in_direction(bunny_row, bunny_col, move):
        collections[move] = collect_in_direction(bunny_row, bunny_col, move)


largest_sum, largest_sum_collection = get_largest_sum(collections)


for direction, collected in largest_sum_collection.items():
    print(direction)
    total_eggs = 0
    for this in collected:
        print(this)
print(largest_sum)
