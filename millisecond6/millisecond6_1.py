with open("input") as file:
    mem_list = list(map(lambda x: int(x), file.read().split("\t")))
    prev_configurations = []
    cycles = 0
    while mem_list not in prev_configurations:
        prev_configurations.append(mem_list[:])
        value = max(mem_list)
        index = mem_list.index(value)
        mem_list[index] = 0
        while value > 0:
            index += 1
            if index == len(mem_list):
                index = 0
            mem_list[index] += 1
            value -= 1
        cycles += 1
    print(cycles)
