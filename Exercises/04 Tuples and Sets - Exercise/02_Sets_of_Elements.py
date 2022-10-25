n, m = [int(x) for x in input().split()]
s1 = set()
s2 = set()


for nn in range(n):
    s1.add(int(input()))
for mm in range(m):
    s2.add(int(input()))

s3 = s1 & s2

print(*s3, sep="\n")
