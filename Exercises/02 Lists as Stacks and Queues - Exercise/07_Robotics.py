import datetime
from collections import deque


class Factory:
    robots = []
    staring_time = None
    products_on_line = deque()

    def __init__(self, name: str, process_time: int):
        self.name = name
        self.process_time = process_time
        self.busy_until = self.staring_time

    def getting_item(self):
        self.busy_until = self.staring_time + datetime.timedelta(0, self.process_time)

    @staticmethod
    def adding_time():
        Factory.staring_time += datetime.timedelta(0, 1)


robot_data_list = input().split(";")
hours, minutes, seconds = [int(x) for x in input().split(":")]
Factory.staring_time = datetime.datetime(100, 1, 1, hours, minutes, seconds)
product = input()

while product != "End":
    Factory.products_on_line.append(product)
    product = input()

for robot_data in robot_data_list:
    name, process = [int(x) if x.isdigit() else x for x in robot_data.split("-")]
    Factory.robots.append(Factory(name, process))

while Factory.products_on_line:
    Factory.adding_time()
    item = Factory.products_on_line.popleft()

    for robot in Factory.robots:
        if Factory.staring_time >= robot.busy_until:
            robot.getting_item()
            print(f'{robot.name} - {item} [{Factory.staring_time.time()}]')
            break
    else:
        Factory.products_on_line.append(item)


#credit: CEO