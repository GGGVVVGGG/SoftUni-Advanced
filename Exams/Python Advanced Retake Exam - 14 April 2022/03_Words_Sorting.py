def words_sorting(*args):
    dict_ = {}
    total = 0
    for this in args:
        sum_ = 0
        for ch in this:
            sum_ += ord(ch)
            total += ord(ch)
        dict_[this] = sum_
    r = []
    if total % 2 != 0:
        for k, v in sorted(dict_.items(), key=lambda xv: -xv[1]):
            r.append(f'{k} - {v}')
        return "\n".join(r)
    else:
        for k, v in sorted(dict_.items()):
            r.append(f'{k} - {v}')
        return "\n".join(r)