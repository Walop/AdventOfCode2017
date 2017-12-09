with open("input") as file:
    prev = ''
    garbage = False
    sum = 0
    for char in file.read():
        if prev != '!':
            if char == '>':
                garbage = False
            elif not garbage and char == '<':
                garbage = True
            elif garbage and char != '!':
                sum += 1
        if prev == '!':
            prev = ''
        else:
            prev = char
    print(sum)