# not giving the correct answer
number_list = list(range(0, 256))
with open("input") as file:
    input_list = [ord(c) for c in ""] + [17, 31, 73, 47, 23]
    curr = 0
    skip = 0
    for i in range(0, 64):
        for length in input_list:
            if length != 0:
                end = curr + length
                end = end % len(number_list)
                if end == 0:
                    number_list = number_list[:curr] + \
                                  list(reversed(number_list[curr:]))
                elif end > curr:
                    number_list = number_list[:curr] +\
                                  list(reversed(number_list[curr:end])) +\
                                  number_list[end:]
                else:
                    l1 = list(reversed(number_list[curr:] + number_list[:end]))
                    number_list = l1[-end:] + number_list[end:curr] + l1[:-end]
            curr += length + skip
            curr = curr % len(number_list)
            skip += 1
    dense_list = []
    for block_start in range(0, 256, 16):
        number = 0
        block = number_list[block_start:block_start+16]
        for num in block:
            number = number ^ number_list[num]
        dense_list.append(number)
    hex_formatted = "".join(["{:02x}".format(hx) for hx in dense_list])
    # should give a2582a3a0e66e6e86e3812dcb672a272 of empty string
    print(hex_formatted)
