def even_odd_filter(**kwargs):
    r = {}
    for k, v in kwargs.items():
        r[k] = []
        for this in v:
            if k == "odd":
                if int(this) % 2 != 0:
                    r[k].append(int(this))
            elif k == "even":
                if int(this) % 2 == 0:
                    r[k].append(int(this))
    return dict(sorted(r.items(), key=lambda x: -len(x[1])))