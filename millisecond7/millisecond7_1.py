with open("input") as file:
    lines = file.read().split("\n")
    progs = [line.split(" ")[0] for line in lines]
    references = [r2 for r3 in [r1[1] for r1 in [line.split(" -> ") for line in lines] if len(r1) == 2] for r2 in r3.split(", ")]
    for prog in progs:
        if prog not in references:
            print(prog)
    
