import math

def split_grid(grid):
    splitted = []
    if len(grid) % 2 == 0:
        step = 2
    else:
        step = 3
    for i in range(0, len(grid), step):
        for j in range(0, len(grid[i]), step):
            piece = []
            for k in range(0, step):
                piece.append([])
                for l in range(0, step):
                    piece[k].append(grid[i+k][j+l])
            splitted.append(piece.copy())
    return splitted

def flatten(arr):
    flat = []
    for a in arr:
        flat.extend(a.copy())
    return flat

def reverse_rows(arr):
    r = []
    for a in arr:
        r.append(list(reversed(a.copy())))
    return r

def reverse_columns(arr):
    r = []
    for a in reversed(arr):
        r.append(a.copy())
    return r

def rotate_left(arr):
    r = []
    for n in range(0,len(arr)):
        r.append([None]*len(arr))
    for y,a in enumerate(arr):
        for x,b in enumerate(a):            
            x2 = y
            y2 = len(a)-1-x
            r[y2][x2] = arr[y][x]
    return r

def rotate_right(arr):
    r = []
    for n in range(0,len(arr)):
        r.append([None]*len(arr))
    for y,a in enumerate(arr):
        for x,b in enumerate(a):            
            x2 = len(a)-1-y
            y2 = x
            r[y2][x2] = arr[y][x]
    return r


def find_from_rule(piece: list[list[str]], rules_from: list[list[list[str]]]) -> int:
    flat = flatten(piece)
    for i, rule in enumerate(rules_from):
        if len(flatten(rule)) != len(flat):
            continue
        a = flatten(rule)
        if flat == a:
            return i
        r0 = reverse_rows(rule)
        if flat == flatten(r0):
            return i
        r1 = rotate_right(rule)
        if flat == flatten(r1):
            return i
        r2 = reverse_rows(r1)
        if flat == flatten(r2):
            return i
        r3 = rotate_right(r1)
        if flat == flatten(r3):
            return i
        r4 = reverse_rows(r3)
        if flat == flatten(r4):
            return i
        r5 = rotate_right(r3)
        if flat == flatten(r5):
            return i
        r6 = reverse_rows(r5)
        if flat == flatten(r6):
            return i
        
    
    raise Exception("No rule matched")
        

def transform(grid: list[list[str]], rules_from: list[list[list[str]]], rules_to: list[list[str]]) -> list[list[str]]:
    sgrid = split_grid(grid)
    transformed = []
    for piece in sgrid:
        # print_grid(piece)
        rule_idx = find_from_rule(piece, rules_from)
        transformed.append(rules_to[rule_idx])
    new_grid = []
    side_length = int(math.sqrt(len(transformed)))
    for i in range(0, side_length):
        for k in range(0, len(transformed[0][0])):
            new_row = []
            for j in range(0,side_length):
                new_row.extend(transformed[i*side_length+j][k])
            new_grid.append(new_row)

    return new_grid

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell,end='')
        print()

def main():
    grid = [list(line) for line in ".#./..#/###".split("/")]
    with open("input") as file:
        rules = [line.split(" => ") for line in file.read().splitlines()]
        rules_from = []
        rules_to = []
        for rule in rules:
            f = [list(x) for x in rule[0].split("/")]
            t = [list(x) for x in rule[1].split("/")]
            rules_from.append(f)
            rules_to.append(t)

    for n in range(0,5):
        grid = transform(grid, rules_from, rules_to)
        print()
        print_grid(grid)

    count = 0
    for row in grid:
        for cell in row:
            if cell=="#":
                count+=1

    print(count)



if __name__ == '__main__':
    main()
