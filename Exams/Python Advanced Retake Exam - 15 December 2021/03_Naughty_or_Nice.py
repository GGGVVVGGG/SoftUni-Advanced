def naughty_or_nice_list(kids, *args, **kwargs):
    result_list = {"Nice": [], "Naughty": [], "Not found": []}
    kid_numbers = [x[0] for x in kids]
    for command in args:
        num, type_ = [int(i) if i.isdigit() else i for i in command.split("-")]
        for kid in kids:
            if num == int(kid[0]) and kid_numbers.count(num) == 1:
                result_list[type_].append(kid[1])
                kids.remove((num, kid[1]))

    kid_names = [x[1] for x in kids]
    for name, type_ in kwargs.items():
        for kid in kids:
            if name == kid[1] and kid_names.count(name) == 1:
                result_list[type_].append(kid[1])
                kids.remove(kid)
    if kids:
        [result_list["Not found"].append(kid[1]) for kid in kids]
    result = [f'{k}: {", ".join(v)}' for k, v in result_list.items() if v]
    return "\n".join(result)

# Test Cases
# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))
# print("=====================")
# print()
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))
# print("=====================")
# print()
# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))
