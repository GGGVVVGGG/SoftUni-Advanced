def recursive_power(param, param1):
    if param1 == 0:
        return 1
    return param * recursive_power(param, param1 -1)