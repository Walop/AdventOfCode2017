with open("input") as file:
    prev = ''
    garbage = False
    depth = 0
    sum = 0
    for char in file.read():
        if prev != '!':
            if char == '>':
                garbage = False
            elif char == '<':
                garbage = True
            elif not garbage:
                if char == '{':
                    depth += 1
                elif char == '}':
                    sum += depth
                    depth -=1
        if prev == '!':
            prev = ''
        else:
            prev = char
    print(sum)