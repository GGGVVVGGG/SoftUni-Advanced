from collections import deque


def check_match():
    for k, chs in TARGETS.items():
        if k == "".join(chs):
            return k, True
    return None, False


TARGETS = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

win = False

vowels = deque(x for x in input().split())
consonants = deque(x for x in input().split())

while vowels and consonants:
    v, c = vowels.popleft(), consonants.pop()
    for target in TARGETS.keys():
        TARGETS[target] = TARGETS[target].replace(v, "")
        TARGETS[target] = TARGETS[target].replace(c, "")
        if TARGETS[target] == '':
            print("Word found:", target)
            win = True
            break
    if win:
        break

if not win:
    print(f"Cannot find any word!")
if vowels:
    print("Vowels left:", *vowels)
if consonants:
    print("Consonants left:", *consonants)