matrix = [[x for x in input()] for x in range(int(input()))]
symb = input()
result =''

for index in range(len(matrix)):
    if symb in matrix[index]:
        result = (index, matrix[index].index(symb))
        break

print(result if result else f'{symb} does not occur in the matrix')