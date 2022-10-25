sub = input().split("|")

while sub:
    this = sub.pop().split()
    if this:
        print(*this, end=" ")