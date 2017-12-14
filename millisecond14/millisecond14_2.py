def knot_hash(input_string):
    number_list = list(range(0, 256))
    input_list = [ord(c) for c in input_string.strip()] + [17, 31, 73, 47, 23]
    input_list *= 64
    curr = 0
    skip = 0
    for length in input_list:
        number_list = number_list[curr:] + number_list[:curr]
        number_list = list(reversed(number_list[:length])) + number_list[length:]
        number_list = number_list[-curr:] + number_list[:-curr]
        curr += length + skip
        curr = curr % len(number_list)
        skip += 1
    dense_list = []
    for block_start in range(0, 256, 16):
        number = 0
        block = number_list[block_start:block_start + 16]
        for num in block:
            number = number ^ num
        dense_list.append(number)
    bin_formatted = "".join(["{:08b}".format(hx) for hx in dense_list])
    return bin_formatted


def search_islands(islands, x, y):
    for index, island in enumerate(islands):
        for cell in island:
            if cell[0] == y and cell[1] == x:
                return index
    return None


def island_finder(mem_map):
    islands = []
    map_width = len(mem_map[0])
    for y, row in enumerate(mem_map):
        for x, cell in enumerate(row):
            if cell == '1':
                if x > 0:
                    index = search_islands(islands, x-1, y)
                    if index is not None:
                        islands[index].append([y, x])
                        if y > 0:
                            index2 = search_islands(islands, x, y-1)
                            if index2 is not None and index != index2:
                                islands[index] += list(islands[index2])
                                del islands[index2]
                        continue
                if y > 0:
                    index = search_islands(islands, x, y-1)
                    if index is not None:
                        islands[index].append([y, x])
                        if x > 0:
                            index2 = search_islands(islands, x-1, y)
                            if index2 is not None and index != index2:
                                islands[index] += list(islands[index2])
                                del islands[index2]
                        continue
                islands.append([[y, x]])
    print(islands)
    return islands


def main():
    input_string = input() + "-"
    mem_map = list()
    for i in range(0, 128):
        mem_map.append(list(knot_hash(input_string+ str(i))))
    regions = island_finder(mem_map)
    print(len(regions))


main()
