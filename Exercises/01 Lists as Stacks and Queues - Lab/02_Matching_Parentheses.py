task = input()
positions = []
for i in range(len(task)):
    if task[i] == "(":
        positions.append(i)
    elif task[i] == ")":
        start = positions.pop()
        print(task[start: i + 1])