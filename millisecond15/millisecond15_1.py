rngA = int(input("Seed for A: "))
rngB = int(input("Seed for B: "))

match16low = 0

for i in range(0,40000000):
    rngA = rngA * 16807 % 2147483647
    rngB = rngB * 48271 % 2147483647
    binA = bin(rngA)
    binB = bin(rngB)
    if binA[-16:] == binB[-16:]:
        match16low += 1
print(match16low)
