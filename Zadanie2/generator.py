import random


def generate_hairpin():
    r = random.randint(1, 4)
    return "(" * r + "." * random.randint(1, 5) + ")" * r


def generate_bulge():
    bulge_type = random.randint(0, 100)
    return "(" + "." * random.randint(1, 5) + "(" if bulge_type < 51 else ")" + "." * random.randint(1, 5) + ")"


def generate_junction(complexity):
    junction = "(" + "." * random.randint(0, 5)
    for i in range(complexity - 1):
        junction += "()" + "." * random.randint(1, 8)
    junction += ")"
    return junction


def generate_pseudoknot(complexity):
    if complexity == ord("A") - 3:
        return "[" + "." * random.randint(0, 3) + "]"
    elif complexity == ord("A") - 2:
        return "{" + "." * random.randint(0, 3) + "}"
    elif complexity == ord("A") - 1:
        return "<" + "." * random.randint(0, 3) + ">"
    else:
        return chr(complexity) + "." * random.randint(0, 3) + chr(complexity + 32)


def randomizer():
    hairpins = random.randint(1, 6)
    hp = []
    for hairpin in range(hairpins):
        hp.append(generate_hairpin())

    bulges = random.randint(1, 6)
    bd = []
    for bulge in range(bulges):
        bd.append(generate_bulge())

    junctions = random.randint(1, 3)
    ju = []
    for i in range(junctions):
        junction = random.randint(3, 8)
        ju.append(generate_junction(junction))

    complexity = random.randint(ord("A") - 3, ord("C"))
    ps = []
    for i in range(ord("A") - 3, complexity + 1):
        c = random.randint(1, 1)
        for j in range(0, c):
            ps.append(generate_pseudoknot(i))

    gen = ""
    elements = []
    elements.extend(hp)
    elements.extend(bd)
    elements.extend(ju)
    elements.extend(ps)
    while True:
        if not elements:
            break
        r = random.randint(0, len(elements) - 1)
        element = elements.pop(r)
        gen += element

    return gen


def generator():
    """
    Function returns a random string in dot-bracket notation from all available possible entries or randomly generated.
    
    :return:    Dot-bracket notation string
    :rtype:     string
    """
    task_list = [
        "((((...((())).....((()))..(()).........))))((.{}[][]{}Aa((..))",
        "((((((..((([]..()()()()()......))).(((((..{}...))))).....(((((.Aa....)))))))))))).Bb.",

    ]

    r = random.randint(0, 100)
    if r > 20:
        return randomizer()
    else:
        element = random.randint(0, len(task_list) - 1)
        return task_list[element]
