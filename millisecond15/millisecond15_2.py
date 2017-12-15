rngA = 618 #int(input("Seed for A: "))
rngB = 814 #int(input("Seed for B: "))

match16low = 0
pairs = 0
binA = None
binB = None
while pairs < 5000000:
    if binA is None:
        rngA = rngA * 16807 % 2147483647
        if rngA % 4 == 0:
            binA = bin(rngA)
    if binB is None:
        rngB = rngB * 48271 % 2147483647
        if rngB % 8 == 0:
            binB = bin(rngB)
    if binA is not None and binB is not None:
        pairs += 1
        if binA[-16:] == binB[-16:]:
            match16low += 1
        binA = None
        binB = None
print(match16low)
