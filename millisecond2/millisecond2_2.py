with open("input", "r") as file:
    input = file.read()
    sum = 0
    for row in input.split("\n"):
        previous_values = []
        for cell in row.split("\t"):
            value = int(cell)
            div = -1
            for pval in previous_values:
                if pval % value == 0:
                    div = pval / value
                    break
                if value % pval == 0:
                    div = value / pval
                    break
            if div > -1:
                break
            previous_values.append(value)
        sum += div
    print(sum)
