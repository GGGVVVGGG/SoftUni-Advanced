s1 = {int(x) for x in input().split()}
s2 = {int(x) for x in input().split()}

n = int(input())
for _ in range(n):
    command, set_nr, *param = input().split()
    if command == "Add":
        if set_nr == "First":
            [s1.add(int(x)) for x in param]
        elif set_nr == "Second":
            [s2.add(int(x)) for x in param]
    elif command == "Remove":
        if set_nr == "First":
            [s1.discard(int(x)) for x in param]
        elif set_nr == "Second":
            [s2.discard(int(x)) for x in param]
    elif command == "Check":
        print(s1.issubset(s2) or s2.issubset(s1))

print(", ".join([str(x) for x in sorted(s1)]))
print(", ".join([str(x) for x in sorted(s2)]))