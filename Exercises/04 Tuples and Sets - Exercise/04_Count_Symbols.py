line = input()
ch = {}

for char in line:
    if char not in ch:
        ch[char] = 0
    ch[char] += 1

for item, value in sorted(ch.items()):
    print(f"{item}: {value} time/s")