with open("input") as file:
    input_list = list(map(lambda x: int(x), file.read().split("\n")))
    index = 0
    jumps = 0
    while index > -1 and index < len(input_list):
        jumps += 1
        next_index = index + input_list[index]
        input_list[index] += 1 if input_list[index] < 3 else -1
        index = next_index
    print(jumps)
        
