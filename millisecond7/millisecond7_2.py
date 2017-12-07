# Just keep piling crap on until it works

class Program:
    def __init__(self, name, weight, refs):
        self.name = name
        self.weight = weight
        self.refs = refs
        self.children = []
        self.parent = None

    def totalweight(self):
        return self.weight + sum([c.totalweight() for c in self.children])

    def balanced(self):
        if len(self.children) == 0:
            return True
        return all(c.totalweight() == self.children[0].totalweight() for c in self.children)
    def frombottom(self):
        if self.parent == None:
            return 0
        return self.parent.frombottom() + 1

with open("input") as file:
    lines = file.read().split("\n")
    progs = []
    for line in lines:
        t1 = line.split(" -> ")
        t2 = t1[0].split(" (")
        name = t2[0]
        weight = int(t2[1][:-1])
        refs = []
        if len(t1) == 2:
            refs = t1[1].split(", ")
        progs.append(Program(name, weight, refs))
    for prog in progs:
        for ref in prog.refs:
            child_prog = next((p for p in progs if p.name == ref), None)
            if child_prog != None:
                prog.children.append(child_prog)
                child_prog.parent = prog
    unbalanced = [prog for prog in progs if not prog.balanced()]
    problem_parent = sorted(unbalanced, key = lambda u: u.frombottom())[-1]
    problem_children = sorted(problem_parent.children, key = lambda c: c.totalweight())
    correct_weight = 0
    if problem_children[0].totalweight() != problem_children[1].totalweight():
        correct_weight = problem_children[1].totalweight() - problem_children[0].totalweight() + problem_children[0].weight
    else:
        correct_weight = problem_children[0].totalweight() - problem_children[-1].totalweight() + problem_children[-1].weight
    print(correct_weight)
        
