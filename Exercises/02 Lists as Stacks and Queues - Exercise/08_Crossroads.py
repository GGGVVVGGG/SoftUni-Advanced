from _collections import deque

duration_green = int(input())
window = int(input())
line = input()
cars = deque()
cars_counter = 0
crashed = False

while line != "END":
    if line == "green":
        if cars:
            current_car = cars.popleft()
            left_seconds = duration_green - len(current_car)

            while left_seconds > 0:
                cars_counter += 1
                if not cars:
                    break
                current_car = cars.popleft()
                left_seconds -= len(current_car)

            if left_seconds == 0:
                cars_counter += 1
            if window >= abs(left_seconds):
                if left_seconds < 0:
                    cars_counter += 1
            else:
                index = window + left_seconds
                print(f"A crash happened!\n{current_car} was hit at {current_car[index]}.")
                crashed = True
                break
    else:
        cars.append(line)
    line = input()

if not crashed:
    print(f"Everyone is safe.\n{cars_counter} total cars passed the crossroads.")

# credit CEO