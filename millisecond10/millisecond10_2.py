number_list = list(range(0, 256))
with open("input") as file:
    input_list = [ord(c) for c in file.read().strip()] + [17, 31, 73, 47, 23]
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
        block = number_list[block_start:block_start+16]
        for num in block:
            number = number ^ num
        dense_list.append(number)
    hex_formatted = "".join(["{:02x}".format(hx) for hx in dense_list])
    print(hex_formatted)
