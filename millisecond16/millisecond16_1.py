with open("input") as file:
    progs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    moves = file.read().strip().split(",")
    for move in moves:
        if move[0] == 's':
            count = int(move[1:])
            progs = progs[-count:] + progs[:-count]
        else:
            positions = []
            if move[0] == 'x':
                positions = [int(pos) for pos in move[1:].split("/")]
            if move[0] == 'p':
                positions = [progs.index(name) for name in move[1:].split("/")]
            a = progs[positions[0]]
            b = progs[positions[1]]
            progs[positions[0]] = b
            progs[positions[1]] = a
    print("".join(progs))
