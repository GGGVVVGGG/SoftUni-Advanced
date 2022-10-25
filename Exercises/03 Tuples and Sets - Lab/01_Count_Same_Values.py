def counter(a):
    r= {}
    for n in a:
        if n not in r.keys():
            r[n] = 0
        r[n] += 1
    return r


res = counter(list(map(float, input().split())))
for num,times in res.items():
    print(f"{num:.1f} - {times} times")