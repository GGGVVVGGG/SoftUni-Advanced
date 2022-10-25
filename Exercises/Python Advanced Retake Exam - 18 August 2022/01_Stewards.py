from collections import deque

seats = input().split(", ")
seq_one = deque(input().split(", "))
seq_two = deque(input().split(", "))
counter = 0

matches = []

while counter < 10 and len(matches) < 3:
    seq_one_num = seq_one.popleft()
    seq_two_num = seq_two.pop()
    counter += 1
    char = chr(int(seq_one_num) + int(seq_two_num))
    try_one = f'{seq_one_num}{char}'
    try_two = f'{seq_two_num}{char}'
    if try_one not in seats and try_two not in seats:
        seq_one.append(seq_one_num)
        seq_two.appendleft(seq_two_num)
        continue
    if try_one in seats and try_one not in matches:
        matches.append(try_one)
    elif try_two in seats and try_two not in matches:
        matches.append(try_two)

print("Seat matches:", ", ".join(matches))
print("Rotations count:", counter)