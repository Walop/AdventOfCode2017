import time

steps = int(input())
pos = 0
after_zero = 0
start = time.perf_counter()
for i in range(1, 50000001):
    if i % 10000000 == 0:
        print(i, time.perf_counter() - start)
    pos = (pos + steps) % i + 1
    if pos == 1:
        after_zero = i
print(after_zero)