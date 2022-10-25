from collections import deque

nums = input().split()
result = deque()

for el in nums:
    if el in "+-*/":
        while len(result) > 1:
            first = result.popleft()
            second = result.popleft()

            if el == "+":
                result.appendleft(first + second)
            elif el == "-":
                result.appendleft(first - second)
            elif el == "*":
                result.appendleft(first * second)
            elif el == "/":
                result.appendleft(first // second)
    else:
        result.append(int(el))

print(*result)