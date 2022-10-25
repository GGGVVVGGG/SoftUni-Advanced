rows, columns = [int(x) for x in input().split()]
string = input()
while len(string) < rows * columns:
    string += string

counter = 0
for _ in range(rows):
    if counter == 1:
        current = string[:columns]
        string = string[columns:]
        print(current[::-1])
        counter = 0
    else:
        current = string[:columns]
        string = string[columns:]
        print(current)
        counter += 1


# rows, columns = [int(x) for x in input().split()]
#
# string = input()
# string *= int(rows * columns / len(string)) + 1
#
# counter = 0
# for _ in range(rows):
#     current = string[:columns]
#     string = string[columns:]
#     if counter == 1:
#         print(current[::-1])
#         counter = 0
#     else:
#         print(current)
#         counter += 1