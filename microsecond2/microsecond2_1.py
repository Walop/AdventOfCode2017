with open("input", "r") as file:
    input = file.read()
    sum = 0
    for row in input.split("\n"):
        min = 0
        max = 0
        for cell in row.split("\t"):
            value = int(cell)
            if value < min or min == 0:
                min = value
            if value > max:
                max = value
        print(min, max)
        sum += max - min
    print(sum)
