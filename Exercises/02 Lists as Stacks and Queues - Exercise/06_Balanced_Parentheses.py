line = input()
opening = "{[("
complete = "{}[]()"
ob = []
good = True

for ch in line:
    if ch in opening:
        ob.append(ch)
    elif not ob:
        good = False
        break
    else:
        lob = ob.pop()
        if f"{lob}{ch}" not in complete:
            good = False
            break


print("YES" if good and not ob else "NO")