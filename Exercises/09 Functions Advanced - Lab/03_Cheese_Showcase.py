def sorting_cheeses(**kwargs):
    r = ''
    for k, v in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        r += k + "\n"
        r += "\n".join([str(i) for i in sorted(v, reverse=True)]) + "\n"

    return r