import itertools

class moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0,0,0]
        # self.history = set()

    def add_velocity(self, moon):
        for axis in range(3):
            if moon.pos[axis] > self.pos[axis]:
                self.vel[axis] += 1
            elif moon.pos[axis] < self.pos[axis]:
                self.vel[axis] -= 1

    def apply_velocity(self):
        for i in range(3):
            self.pos[i] += self.vel[i]
        '''
        curr_history = len(self.history)
        self.history.add(tuple(self.pos))
        if curr_history == len(self.history):
            return True
        return False
        '''

    def energy(self):
        return sum([abs(n) for n in self.pos]) * sum([abs(n) for n in self.vel])

    def __str__(self):
        return f"<x={self.pos[0]}, y={self.pos[1]}, z={self.pos[2]}> <x={self.vel[0]}, y={self.vel[1]}, z={self.vel[2]}>"

moons = list()
for line in open("input.txt").read().strip().split('\n'):
    moons.append(moon([int(n[2:]) for n in line[1:-1].split(', ')]))


for moon in moons:
    print(str(moon))

steps = 0
while steps < 1000:
    # shitty double loop
    for moon in moons:
        other_moons = moons[:]
        other_moons.remove(moon)
        for other_moon in other_moons:
            moon.add_velocity(other_moon)
    for moon in moons:
        moon.apply_velocity()
    '''
    same = True
    for moon in moons:
        same = same and moon.apply_velocity()
    if same:
        break
        '''
    steps += 1

print()
for moon in moons:
    print(str(moon))

print(sum([moon.energy() for moon in moons]))
