inputs = [o for o in open("input.txt").read().strip().split("\n")]

class planet:
    def __init__(self, name: str, last):
        self.name = name
        self.last = last

planets = list()
def find_planet(name):
    for p in planets:
        if p != None and name == p.name:
            return p

for pair in inputs:
    pair = pair.split(')')

    orbitee = find_planet(pair[0])
    if orbitee == None:
        orbitee = planet(pair[0], None)
        planets.append(orbitee)
    orbiter = find_planet(pair[1])
    if orbiter == None:
        orbiter = planet(pair[1], orbitee)
        planets.append(orbiter)
    else:
        orbiter.last = orbitee

san = []
for p in planets:
    if p != None and p.name == "SAN":
        plan = p.last
        while plan != None:
            if plan.last == None:
                break
            san.append(plan.name)
            plan = plan.last


path = 0
common = ''
for p in planets:
    if p != None and p.name == "YOU":
        plan = p.last
        while plan != None:
            if plan.last == None:
                break
            if plan.name in san:
                common = plan.name
                break
            path += 1
            plan = plan.last
path += san.index(common)
print(path)
