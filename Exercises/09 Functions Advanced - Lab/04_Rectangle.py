def rectangle(param, param1):
    if type(param) != int or type(param1) != int:
        return "Enter valid values!"

    def area(param, param1):
        return param * param1

    def perimeter(param, param1):
        return (param + param1) * 2

    return f"Rectangle area: {area(param, param1)}" + "\n" + f"Rectangle perimeter: {perimeter(param, param1)}"