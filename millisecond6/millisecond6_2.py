def redistribute(mem_list):
    value = max(mem_list)
    index = mem_list.index(value)
    mem_list[index] = 0
    while value > 0:
        index += 1
        if index == len(mem_list):
            index = 0
        mem_list[index] += 1
        value -= 1
    return mem_list
            

with open("input") as file:
    mem_list = list(map(lambda x: int(x), file.read().split("\t")))
    prev_configurations = []
    while mem_list not in prev_configurations:
        prev_configurations.append(mem_list[:])
        redistribute(mem_list)
    inf_config = mem_list[:]
    redistribute(mem_list)
    cycles = 1
    while mem_list != inf_config:
        redistribute(mem_list)
        cycles += 1
    print(cycles)
