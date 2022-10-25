def concatenate(*args, **kwargs):
    string = "".join(args)
    for k, v in kwargs.items():
        if k in string:
            string = string.replace(k, v)
    return string