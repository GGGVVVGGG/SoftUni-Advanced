def func_executor(*args):
    result = ""
    for func_name, func_arg in args:
        result += f"{func_name.__name__} - {func_name(*func_arg)}\n"
    return result

# credit CEO
