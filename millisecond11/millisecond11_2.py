with open("input") as file:
    child_steps = file.read().strip().split(",")
    move = {
        "n": lambda pos: (pos[0]-1, pos[1]+1),
        "ne": lambda pos: (pos[0], pos[1]+1),
        "se": lambda pos: (pos[0]+1, pos[1]),
        "s": lambda pos: (pos[0]+1, pos[1]-1),
        "sw": lambda pos: (pos[0], pos[1]-1),
        "nw": lambda pos: (pos[0]-1, pos[1]),
    }
    pos = (0, 0)
    furthest = 0
    for step in child_steps:
        pos = move[step](pos)
        distance = max(abs(pos[0]), abs(pos[1]))
        if distance > furthest:
            furthest = distance
    print(furthest)
