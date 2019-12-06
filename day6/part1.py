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

count = 0
for p in planets:
    if p != None:
        print(f"chain for planet {p.name}:")
    plan = p
    while plan != None:
        print(plan.name)
        if plan.last == None:
            break
        count += 1
        plan = plan.last
print(count)
