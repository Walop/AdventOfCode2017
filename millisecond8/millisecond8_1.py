with open("input") as file:
    lines = [line.split(" ") for line in file.read().strip().split("\n")]
    register_names = set([line[0] for line in lines])
    registers = {}
    for name in register_names:
        registers[name] = 0
    operations = {
        "dec": lambda r,v: r-v,
        "inc": lambda r,v: r+v }
    comparisons = {
        ">": lambda a,b: a > b,
        ">=": lambda a,b: a >= b,
        "<": lambda a,b: a < b,
        "<=": lambda a,b: a <= b,
        "==": lambda a,b: a == b,
        "!=": lambda a,b: a != b }
    for line in lines:
        if comparisons[line[5]](registers[line[4]],int(line[6])):
            registers[line[0]] = operations[line[1]](registers[line[0]],int(line[2]))
    print(max(registers.values()))
