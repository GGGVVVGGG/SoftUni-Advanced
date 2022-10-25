from collections import deque

presents = {150: "Doll",
            250: "Wooden train",
            300: "Teddy bear",
            400: "Bicycle"
            }

materials = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())
crafted = {}

while materials and magics:
    material = materials.pop()
    magic = magics.popleft()
    result = material * magic

    if result in presents:
        toy = presents[result]
        if toy in crafted:
            crafted[toy] += 1
        else:
            crafted[toy] = 1
    else:
        if result < 0:
            materials.append(material + magic)
        elif result > 0:
            materials.append(material + 15)
        else:
            if material == 0 and magic == 0:
                continue
            if material == 0:
                magics.appendleft(magic)
            if magic == 0:
                materials.append(material)

if "Wooden train" in crafted and "Doll" in crafted or "Teddy bear" in crafted and "Bicycle" in crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

for k, v in sorted(crafted.items()):
    print(f"{k}: {v}")