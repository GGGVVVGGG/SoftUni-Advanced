clothes = list(map(int, input().split()))
cpct = int(input())

used_racks = 1
cur_cpct = cpct

while clothes:
    current_cloth = clothes[-1]

    if current_cloth <= cur_cpct:
        clothes.pop()
        cur_cpct -= current_cloth
    else:
        used_racks += 1
        cur_cpct = cpct

print(used_racks)