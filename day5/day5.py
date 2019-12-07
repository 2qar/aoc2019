import operator

onums = [int(num) for num in open('input.txt').read().strip().split(',')]

jumps = {1: 4, 
        2: 4, 
        3: 2, 
        4: 2, 
        5: 3,
        6: 3,
        7: 4, 
        8: 4}

addmul = lambda op : operator.add if op == 1 else operator.mul
jumpif = lambda op : operator.ne if op == 5 else operator.eq
trufal = lambda op : operator.lt if op == 7 else operator.eq

def test(innum: int):
    nums = onums[:]
    i = 0
    while i < len(nums):
        opcode = nums[i] % 100
        args = []
        modes = nums[i] // 10 // 10
        argc = 0
        while argc < jumps[opcode]-1:
            if modes % 10 == 1:
                args.append(nums[i+argc+1])
            else:
                args.append(nums[nums[i+argc+1]])
            modes //= 10
            argc += 1
        if opcode in (1,2):
            nums[nums[i+3]] = addmul(opcode)(args[0],args[1])
        elif opcode == 3:
            nums[nums[i+1]] = innum
        elif opcode == 4:
            if args[0] != 0:
                return args[0]
        elif opcode in (5,6) and jumpif(opcode)(args[0], 0):
            i = args[1]
            continue
        elif opcode in (7,8):
            nums[nums[i+3]] = int(trufal(opcode)(args[0],args[1]))
        elif opcode == 99:
            break
        i += jumps[opcode]

print(f"Silver: {test(1)}")
print(f"Gold:   {test(5)}")
