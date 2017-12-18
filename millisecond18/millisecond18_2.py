with open("input") as file:
    instructions = [line.split(" ") for line in file.read().splitlines()]
    registers = [{'p': 0}, {'p': 1}]
    i = [0, 0]
    queue = [[], []]
    waiting = [False, False]
    sent = 0
    running = [True, True]
    while running[0] or running[1]:
        if 0 <= i[0] < len(instructions):
            instruction = instructions[i[0]]
            if instruction[1].isalpha():
                if instruction[1] not in registers[0]:
                    registers[0][instruction[1]] = 0
                par1 = registers[0][instruction[1]]
            else:
                par1 = int(instruction[1])
    
            if len(instruction) == 3:
                if instruction[2].isalpha():
                    if instruction[2] not in registers[0]:
                        registers[0][instruction[2]] = 0
                    par2 = registers[0][instruction[2]]
                else:
                    par2 = int(instruction[2])
    
            if instruction[0] == "snd":
                queue[1] = [par1] + queue[1]
            elif instruction[0] == "set":
                registers[0][instruction[1]] = par2
            elif instruction[0] == "add":
                registers[0][instruction[1]] += par2
            elif instruction[0] == "mul":
                registers[0][instruction[1]] *= par2
            elif instruction[0] == "mod":
                registers[0][instruction[1]] %= par2
            elif instruction[0] == "rcv":
                if len(queue[0]) > 0:
                    registers[0][instruction[1]] = queue[0].pop()
                    waiting[0] = False
                else:
                    waiting[0] = True
                    i[0] -= 1
            elif instruction[0] == "jgz" and par1 > 0:
                i[0] += par2 - 1
            i[0] += 1
        else:
            if running[0]:
                print("0 stopped")
            running[0] = False
        if 0 <= i[1] < len(instructions):
            instruction = instructions[i[1]]
            if instruction[1].isalpha():
                if instruction[1] not in registers[1]:
                    registers[1][instruction[1]] = 0
                par1 = registers[1][instruction[1]]
            else:
                par1 = int(instruction[1])

            if len(instruction) == 3:
                if instruction[2].isalpha():
                    if instruction[2] not in registers[1]:
                        registers[1][instruction[2]] = 0
                    par2 = registers[1][instruction[2]]
                else:
                    par2 = int(instruction[2])

            if instruction[0] == "snd":
                queue[0] = [par1] + queue[0]
                sent += 1
            elif instruction[0] == "set":
                registers[1][instruction[1]] = par2
            elif instruction[0] == "add":
                registers[1][instruction[1]] += par2
            elif instruction[0] == "mul":
                registers[1][instruction[1]] *= par2
            elif instruction[0] == "mod":
                registers[1][instruction[1]] %= par2
            elif instruction[0] == "rcv":
                if len(queue[1]) > 0:
                    registers[1][instruction[1]] = queue[1].pop()
                    waiting[1] = False
                else:
                    waiting[1] = True
                    i[1] -= 1
            elif instruction[0] == "jgz" and par1 > 0:
                i[1] += par2 - 1
            i[1] += 1
        else:
            if running[1]:
                print("1 stopped")
            running[1] = False
        if (waiting[0] and waiting[1]) or (waiting[0] and not running[1]) or (waiting[1] and not running[0]):
            running = [False, False]
print(sent)