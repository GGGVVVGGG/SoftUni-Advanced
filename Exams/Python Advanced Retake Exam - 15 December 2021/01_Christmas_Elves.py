from collections import deque

elf_energy = deque([int(x) for x in input().split()])
box_materials_energy_needed = deque([int(x) for x in input().split()])

total_energy_spend = 0
toys_in_the_bag = 0
try_counter = 0

while elf_energy and box_materials_energy_needed:
    current_energy = elf_energy.popleft()
    if current_energy < 5:
        continue

    try_counter += 1
    current_box = box_materials_energy_needed.pop()

    if try_counter % 3 == 0 and try_counter % 5 == 0:
        current_box_m = 2 * current_box
        if current_energy < current_box_m:
            elf_energy.append(current_energy * 2)
            box_materials_energy_needed.append(current_box)
        else:
            elf_energy.append(current_energy - current_box_m)
            total_energy_spend += current_box_m
    elif try_counter % 3 == 0:
        current_box_m = 2 * current_box
        if current_energy < current_box_m:
            elf_energy.append(current_energy * 2)
            box_materials_energy_needed.append(current_box)
        else:
            elf_energy.append(current_energy - (current_box_m - 1))
            total_energy_spend += current_box_m
            toys_in_the_bag += 2
    elif try_counter % 5 == 0:
        if current_energy < current_box:
            elf_energy.append(current_energy * 2)
            box_materials_energy_needed.append(current_box)
        else:
            elf_energy.append(current_energy - current_box)
            total_energy_spend += current_box
    elif current_energy < current_box:
        elf_energy.append(current_energy * 2)
        box_materials_energy_needed.append(current_box)
    else:
        elf_energy.append(current_energy - (current_box - 1))
        total_energy_spend += current_box
        toys_in_the_bag += 1

print(f"Toys:", toys_in_the_bag)
print(f"Energy:", total_energy_spend)
if elf_energy:
    print("Elves left:", ", ".join(str(x) for x in elf_energy))
if box_materials_energy_needed:
    print("Boxes left:", ", ".join(str(x) for x in box_materials_energy_needed))