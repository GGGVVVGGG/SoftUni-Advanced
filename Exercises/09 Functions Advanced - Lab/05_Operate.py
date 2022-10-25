def operate(*args):
    symbol = args[0]
    rest = args[2:]
    r = args[1]

    for this in rest:
        if symbol == "+":
            r += sum(rest)
        elif symbol == "-":
            r -= this
        elif symbol == "*":
            r *= this
        elif symbol == "/":
            r /= this
    return r