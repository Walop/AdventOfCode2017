with open("input") as file:
    instructions = [line.split(" ") for line in file.read().splitlines()]
    registers = {}
    mul_count = 0
    i = 0
    while 0 <= i < len(instructions):
        instruction = instructions[i]
        par1 = 0
        par2 = 0
        if instruction[1].isalpha():
            if instruction[1] not in registers:
                registers[instruction[1]] = 0
            par1 = registers[instruction[1]]
        else:
            par1 = int(instruction[1])

        if len(instruction) == 3:
            if instruction[2].isalpha():
                if instruction[2] not in registers:
                    registers[instruction[2]] = 0
                par2 = registers[instruction[2]]
            else:
                par2 = int(instruction[2])

        if instruction[0] == "set":
            registers[instruction[1]] = par2
        if instruction[0] == "sub":
            registers[instruction[1]] -= par2
        elif instruction[0] == "mul":
            registers[instruction[1]] *= par2
            mul_count += 1
        elif instruction[0] == "jnz" and par1 != 0:
            i += par2
            continue
        i += 1

print(mul_count)