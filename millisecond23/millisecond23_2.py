import math

def is_prime(num):
    if num%2==0:
        return False
    for x in range(3,int(math.sqrt(num)),2):
        if num%x==0:
            return False
    return True


with open("input") as file:
    instructions = [line.split(" ") for line in file.read().splitlines()]
    b = int(instructions[0][2]) * 100 + 100000
    count = 0
    for x in range(0,1001):
        if not is_prime(b):
            count+=1
        b+=17

print(count)