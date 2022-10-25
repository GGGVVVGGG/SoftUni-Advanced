def even_odd(*args):
    r = []
    if args[-1] == "even":
        for item in args[:-1]:
            if int(item) % 2 == 0:
                r.append(int(item))
        return r
    for item in args[:-1]:
        if int(item) % 2 != 0:
            r.append(int(item))
    return r