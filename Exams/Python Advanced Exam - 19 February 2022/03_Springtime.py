def start_spring(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        if v not in new_dict.keys():
            new_dict[v] = [k]
        else:
            new_dict[v].append(k)

    for k in new_dict.keys():
        new_dict[k] = sorted(new_dict[k])

    new_dict = {x: y for x, y in sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0]))}
    r = []
    for k, v in new_dict.items():
        r.append(f'{k}:')
        for item in v:
            r.append(f'-{item}')
    return "\n".join(r)
