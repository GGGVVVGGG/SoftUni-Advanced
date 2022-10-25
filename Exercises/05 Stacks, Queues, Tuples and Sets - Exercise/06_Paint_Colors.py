from collections import deque

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
matched_colors = []

substrings = deque(input().split())

while substrings:
    first_sub = substrings.popleft()
    second_sub = substrings.pop() if substrings else ""

    # match scenario 1
    result = first_sub + second_sub
    if result in main_colors or result in secondary_colors:
        matched_colors.append(result)
        continue

    # match scenario 2
    result = second_sub + first_sub
    if result in main_colors or result in secondary_colors:
        matched_colors.append(result)
        continue

    first_sub = first_sub[:-1]
    second_sub = second_sub[:-1]

    # trimming last digit or deleting if len = 1, and inserting in the middle
    if first_sub:
        substrings.insert(len(substrings) // 2, first_sub)

    if second_sub:
        substrings.insert(len(substrings) // 2, second_sub)

required_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", 'blue']
}

final_list = []

for color in matched_colors:
    requirements_fit = True
    if color in secondary_colors:
        for required in required_colors[color]:
            if required not in matched_colors:
                requirements_fit = False
        if requirements_fit:
            final_list.append(color)
    else:
        final_list.append(color)

print(final_list)