number_list = list(range(0, 256))
with open("input") as file:
    input_list = [int(l) for l in file.read().split(",")]
    curr = 0
    end = 0
    skip = 0
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
    print(number_list[0] * number_list[1])