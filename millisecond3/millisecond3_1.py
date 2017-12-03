#This one is total crap hack, everything is stupid and upside down

import math

input = input("Number to find: ")
number = int(input)
side = math.ceil(math.sqrt(number))
if side % 2 == 0:
    side += 1
x = side
y = 1
curnum = side**2
dx = -1
dy = 0
while number != curnum:
    x += dx
    y += dy
    curnum -= 1
    if x == 1 and y == 1:
        dx = 0
        dy = 1
    elif x == 1 and y == side:
        dx = 1
        dy = 0
    elif x == side and y == side:
        dx = 0
        dy = -1

x = abs(math.ceil(side / 2 - x))
y = abs(math.ceil(side / 2 - y))
print(x+y)
