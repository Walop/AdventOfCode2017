import math
import time

with open("input") as file:
    lines = file.read().splitlines()
    nodes = {}
    height = len(lines)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                x = math.ceil(j - height/2)
                y = math.ceil(i - height/2)
                nodes[str(x) + "_" + str(-y)] = "i"
    pos = (0, 0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    infections = 0
    start = time.perf_counter()
    for i in range(0, 10000000):
        if i % 1000000 == 0:
            print(time.perf_counter() - start, i, infections)
        key = str(pos[0]) + "_" + str(pos[1])
        if key not in nodes:
            nodes[key] = 'w'
            directions = directions[-1:] + directions[:-1]
        else:
            if nodes[key] == 'w':
                nodes[key] = 'i'
                infections += 1
            elif nodes[key] == 'i':
                nodes[key] = 'f'
                directions = directions[1:] + directions[:1]
            elif nodes[key] == 'f':
                del nodes[key]
                directions = directions[2:] + directions[:2]
        pos = (pos[0] + directions[0][0], pos[1] + directions[0][1])
    print(infections)