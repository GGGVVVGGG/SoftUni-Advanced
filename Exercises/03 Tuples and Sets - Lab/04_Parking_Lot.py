n = int(input())
lot = set()
for _ in range(n):
    cmd, nbr = input().split(", ")
    if cmd == "IN":
        # if nbr not in lot:
        lot.add(nbr)
    elif cmd == "OUT":
        # if nbr in lot:
        lot.remove(nbr)

if lot:
    print('\n'.join(lot))
else:
    print("Parking Lot is Empty")