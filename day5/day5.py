with open('input.txt') as f:
    onums = [int(num) for num in f.read().split(',')]

jumps = {1: 4, 
        2: 4, 
        3: 2, 
        4: 2, 
        5: 3,
        6: 3,
        7: 4, 
        8: 4}

def test(innum: int):
    nums = onums[:]
    i = 0
    while i < len(nums) and nums[i] != 99:
        opcode = nums[i]
        args = []
        if len(str(nums[i])) >= 3:
            opnum = nums[i]
            opcode = opnum % 10
            modes = opnum // 10 // 10
            argc = 0
            while argc < jumps[opcode]-1:
                if modes % 10 == 1:
                    args.append(nums[i+argc+1])
                else:
                    args.append(nums[nums[i+argc+1]])
                modes = modes // 10
                argc += 1
        else:
            argc = 1
            while argc < jumps[opcode]:
                args.append(nums[nums[i+argc]])
                argc += 1
        if opcode == 1:
            nums[nums[i+3]] = args[0] + args[1]
        elif opcode == 2:
            nums[nums[i+3]] = args[0] * args[1]
        elif opcode == 3:
            nums[nums[i+1]] = innum
        elif opcode == 4:
            if args[0] != 0:
                return args[0]
        elif opcode == 5 and args[0] != 0:
            i = args[1]
            continue
        elif opcode == 6 and args[0] == 0:
            i = args[1]
            continue
        elif opcode == 7:
            if args[0] < args[1]:
                nums[nums[i+3]] = 1
            else:
                nums[nums[i+3]] = 0
        elif opcode == 8:
            if args[0] == args[1]:
                nums[nums[i+3]] = 1
            else:
                nums[nums[i+3]] = 0
        elif opcode == 99:
            break
        i += jumps[opcode]

print(f"Silver: {test(1)}")
print(f"Gold:   {test(5)}")
