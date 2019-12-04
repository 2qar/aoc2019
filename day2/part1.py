with open('input.txt') as f:
    nums = [int(num) for num in f.read().split(',')]

#nums = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

i = 0
while i < len(nums) and nums[i] != 99:
    if nums[i] == 1:
        nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
    elif nums[i] == 2:
        nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
    elif nums[i] == 99:
        break
    i += 4

print(nums[0])
