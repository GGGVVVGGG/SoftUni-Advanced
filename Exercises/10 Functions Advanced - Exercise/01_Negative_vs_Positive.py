def myfunc(line):
    n, p = [], []
    [n.append(int(i)) if i[0] == "-" else p.append(int(i)) for i in line]
    print(sum(n), sum(p), sep="\n")
    return "The negatives are stronger than the positives" if abs(sum(n)) > sum(p) else "The positives are stronger than the negatives"
print(myfunc(input().split()))