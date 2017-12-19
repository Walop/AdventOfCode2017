with open("input") as file:
    network = [list(line) for line in file.read().splitlines()]
    current_position = [0, network[0].index("|")]
    letters = []
    direction = [1, 0]
    while True:
        current_char = network[current_position[0]][current_position[1]]
        if current_char.isalpha():
            letters.append(current_char)
        elif current_char == '+':
            if direction[0] == 0:
                if network[current_position[0] + 1][current_position[1]] != ' ':
                    direction = [1, 0]
                else:
                    direction = [-1, 0]
            else:
                if network[current_position[0] ][current_position[1] + 1] != ' ':
                    direction = [0, 1]
                else:
                    direction = [0, -1]
        if current_char == ' ':
            break
        current_position = [current_position[0] + direction[0], current_position[1] + direction[1]]
print("".join(letters))
