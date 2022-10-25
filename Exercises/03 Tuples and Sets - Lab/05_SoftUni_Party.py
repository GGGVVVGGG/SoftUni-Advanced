n = int(input())
vip = set()
reg = set()

for _ in range(n):
    g = input()
    if g[0].isdigit():
        vip.add(g)
    else:
        reg.add(g)

g = input()
while g != "END":
    if g[0].isdigit() and g in vip:
        vip.remove(g)
    elif g[0].isalpha() and g in reg:
        reg.remove(g)
    g = input()

result = []

for g in sorted(vip):
    result.append(g)
for g in sorted(reg):
    result.append(g)

print(len(result))
print("\n".join(result))