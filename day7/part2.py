import itertools
import operator

onums = [int(num) for num in open("input.txt").read().strip().split(',')]
#onums = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

jumps = {1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        99: 0}

addmul = lambda op : operator.add if op == 1 else operator.mul
jumpif = lambda op : operator.ne if op == 5 else operator.eq
trufal = lambda op : operator.lt if op == 7 else operator.eq

class amp:
    def __init__(self, nums, phase):
        self.i = 0
        self.nums = nums[:]
        self.phase = phase
        self.done = False

    def run(self, innum: int):
        while self.i < len(self.nums):
            opcode = self.nums[self.i] % 100
            args = []
            modes = self.nums[self.i] // 10 // 10
            argc = 0
            while argc < jumps[opcode]-1:
                if modes % 10 == 1:
                    args.append(self.nums[self.i+argc+1])
                else:
                    args.append(self.nums[self.nums[self.i+argc+1]])
                modes //= 10
                argc += 1

            print(opcode)
            print(args)
            if opcode in (1,2):
                self.nums[self.nums[self.i+3]] = addmul(opcode)(args[0],args[1])
            elif opcode == 3:
                if self.phase != -1:
                    self.nums[self.nums[self.i+1]] = self.phase
                    self.phase = -1
                else:
                    self.nums[self.nums[self.i+1]] = innum
            elif opcode == 4:
                self.i += jumps[opcode]
                return args[0]
            elif opcode in (5,6) and jumpif(opcode)(args[0], 0):
                self.i = args[1]
                continue
            elif opcode in (7,8):
                self.nums[self.nums[self.i+3]] = int(trufal(opcode)(args[0],args[1]))
            elif opcode == 99:
                self.done = True
                print(f"innum: {innum}")
                break
            self.i += jumps[opcode]

# part 2
out = []
innum = 0
for combo in [*itertools.permutations([5,6,7,8,9], 5)]:
    innum = 0
    amps = [amp(onums[:], phase) for phase in combo]
    iters = 0
    while 1:
        done = 0
        for a in amps:
            if a.done:
                done += 1
            f = a.run(innum)
            if f != None:
                innum = f
        if done == 5:
            out.append(innum)
            break
print(out)
print(f"Gold: {max(out)}")
