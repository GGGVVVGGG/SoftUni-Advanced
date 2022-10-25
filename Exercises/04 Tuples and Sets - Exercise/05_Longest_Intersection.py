n = int(input())
results = []
for _ in range(n):

    first_set, second_set = [x for x in input().split("-")]

    first_set = [int(x) for x in first_set.split(",")]
    second_set = [int(x) for x in second_set.split(",")]
    a = set([x for x in range(first_set[0], first_set[1] + 1)])
    b = set([x for x in range(second_set[0], second_set[1] + 1)])
    intersection = a.intersection(b)
    results.append(intersection)

print(f'Longest intersection is {list(sorted(results, key= lambda x: -len(x))[0])} with length {len(sorted(results, key= lambda x: -len(x))[0])}')