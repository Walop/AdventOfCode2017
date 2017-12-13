with open("input") as file:
    entry_list = [entry.split(": ") for entry in file.read().splitlines()]
    scanner_list = [[int(entry[0]), int(entry[1]), 0, True] for entry in entry_list]
    severity = 0
    for layer in range(0, scanner_list[-1][0]+1):
        for scanner in scanner_list:
            if scanner[0] == layer and scanner[2] == 0:
                severity += layer*scanner[1]
            if (scanner[3] and scanner[1]-1 == scanner[2]) or (not scanner[3] and scanner[2] == 0):
                scanner[3] = not scanner[3]
            if scanner[3]:
                scanner[2] += 1
            else:
                scanner[2] -= 1
    print(severity)