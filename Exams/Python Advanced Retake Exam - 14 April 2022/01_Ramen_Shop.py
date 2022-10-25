from collections import deque

ramen = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while ramen and customers:
    ramen_cup = ramen.pop()
    current_customer = customers.popleft()
    if ramen_cup == current_customer:
        continue
    if ramen_cup > current_customer:
        ramen_cup -= current_customer
        ramen.append(ramen_cup)
    elif current_customer > ramen_cup:
        current_customer -= ramen_cup
        customers.appendleft(current_customer)

if not customers:
    print(f"Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left:", ", ".join(str(x) for x in ramen))
if not ramen and customers:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left:", ", ".join(str(x) for x in customers))