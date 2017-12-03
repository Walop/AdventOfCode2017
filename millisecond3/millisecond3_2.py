#Not so pretty, but better than the previous abomination
number = int(input("Number to find: "))

moves = 0
tomove = 1
lastnum = 1
dir = 'r'
cells = [[1,0,0]]
currcoord = [0,0]

while lastnum < number:
    if dir == 'r':
        currcoord = [currcoord[0] + 1, currcoord[1]]
        moves += 1
        if moves == tomove:
            moves = 0
            dir = 'u'
    elif dir == 'u':
        currcoord = [currcoord[0], currcoord[1] + 1]
        moves += 1
        if moves == tomove:
            moves = 0
            dir = 'l'
            tomove += 1
    elif dir == 'l':
        currcoord = [currcoord[0] - 1, currcoord[1]]
        moves += 1
        if moves == tomove:
            moves = 0
            dir = 'd'
    elif dir == 'd':
        currcoord = [currcoord[0], currcoord[1] - 1]
        moves += 1
        if moves == tomove:
            moves = 0
            dir = 'r'
            tomove += 1
    lastnum = 0
    for cell in cells:
        dx = cell[1] - currcoord[0] if cell[1] > currcoord[0] else currcoord[0] - cell[1]
        dy = cell[2] - currcoord[1] if cell[2] > currcoord[1] else currcoord[1] - cell[2]
        if dx < 2 and dy < 2:
            lastnum += cell[0]
    cells.append([lastnum, currcoord[0], currcoord[1]])
print(lastnum)
                 
