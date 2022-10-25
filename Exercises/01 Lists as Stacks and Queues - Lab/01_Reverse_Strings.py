def reverse(string):
    n = len(string)
    stack = []
    for i in range(0, n, 1):
        stack.append(string[i])
    string = ""
    for i in range(0, n, 1):
        string += stack.pop()
    return string


print(reverse(input()))


# or better:
# def reverse(string):
#     return string[::-1]
#
#
# print(reverse(input()))
