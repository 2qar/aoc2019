import operator

onums = [int(num) for num in open("input.txt").read().strip().split(',')]

jumps = {1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 2,
        99: 0}

addmul = lambda op : operator.add if op == 1 else operator.mul
jumpif = lambda op : operator.ne if op == 5 else operator.eq
trufal = lambda op : operator.lt if op == 7 else operator.eq

class amp:
    def __init__(self, nums, phase):
        self.i = 0
        self.nums = nums[:]
        self.base = 0
        self.phase = phase
        self.done = False
        self.output = []

    def run(self, innum: int):
        while self.i < len(self.nums):
            opcode = self.nums[self.i] % 100
            args = []
            modes = self.nums[self.i] // 10 // 10
            argc = 0
            while argc < jumps[opcode]-1:
                if modes % 10 == 2:
                    args.append(self.nums[self.nums[self.i+argc+1]+self.base])
                elif modes % 10 == 1:
                    args.append(self.nums[self.i+argc+1])
                else:
                    args.append(self.nums[self.nums[self.i+argc+1]])
                modes //= 10
                argc += 1

            n = 10
            for i in range(jumps[opcode]-1):
                n *= 10
            addr = self.nums[self.i+jumps[opcode]-1]+self.base if self.nums[self.i] // n == 2 else self.nums[self.i+jumps[opcode]-1]
            if opcode in (1,2):
                self.nums[addr] = addmul(opcode)(args[0],args[1])
            elif opcode == 3:
                if self.phase != -1:
                    self.nums[self.nums[self.i+1]] = self.phase
                    self.phase = -1
                else:
                    self.nums[addr] = innum
            elif opcode == 4:
                self.output.append(args[0])
            elif opcode in (5,6) and jumpif(opcode)(args[0], 0):
                self.i = args[1]
                continue
            elif opcode in (7,8):
                self.nums[addr] = int(trufal(opcode)(args[0],args[1]))
            elif opcode == 9:
                self.base += args[0]
            elif opcode == 99:
                self.done = True
                break
            self.i += jumps[opcode]

def solve(val: int):
    a = amp(onums[:], -1)
    for i in range(1000):
        a.nums.append(0)
    while not a.done:
        a.run(val)
    return a.output

print(f"Silver: {solve(1)}")
print(f"Gold: {solve(2)}")
