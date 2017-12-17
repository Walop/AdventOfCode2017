steps = int(input())
buffer = [0, 1]
pos = 1
for i in range(2, 2018):
    pos = (pos + steps) % len(buffer) + 1
    buffer = buffer[:pos] + [i] + buffer[pos:]
pos_after_last = (pos+1) % len(buffer)
print(buffer[pos_after_last])