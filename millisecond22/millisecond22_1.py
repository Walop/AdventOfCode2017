import math

with open("input") as file:
    lines = file.read().splitlines()
    infected_nodes = []
    height = len(lines)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                x = math.ceil(j - height/2)
                y = math.ceil(i - height/2)
                infected_nodes.append((x, -y))
    pos = (0, 0)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    infections = 0
    for i in range(0, 10000):
        if pos in infected_nodes:
            infected_nodes.remove(pos)
            directions = directions[1:] + directions[:1]
        else:
            infected_nodes.append(pos)
            infections += 1
            directions = directions[-1:] + directions[:-1]
        pos = (pos[0] + directions[0][0], pos[1] + directions[0][1])
    print(infections)