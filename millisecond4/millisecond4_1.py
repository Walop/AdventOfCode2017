import re

with open("input") as file:
    input_txt = file.read()
    phrases = input_txt.split("\n")
    valid = 0
    invalid_re = re.compile(r"(\b\w+\b).*\1")
    for phrase in phrases:
        if invalid_re.search(phrase) == None:
            valid += 1
    print(valid)
