with open('input.txt') as f:
    nums = [int(num) for num in f.read().split(',')]

def process(noun, verb) -> int:
    i = 0
    new = nums.copy()
    new[1] = noun
    new[2] = verb
    while i < len(new) and new[i] != 99:
        if new[i] == 1:
            new[new[i+3]] = new[new[i+1]] + new[new[i+2]]
        elif new[i] == 2:
            new[new[i+3]] = new[new[i+1]] * new[new[i+2]]
        elif new[i] == 99:
            break
        i += 4
    return new[0]

for f in range(100):
    for j in range(100):
        out = process(f, j)
        if out == 19690720:
            print(100 * f + j)
            break
