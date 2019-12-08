import textwrap
import sys

width = 25
height = 6

img = textwrap.wrap(open("input.txt").read().strip(), width * height)

min_zeroes = sys.maxsize
min_layer = None
for layer in img:
    zeroes = layer.count('0')
    if zeroes < min_zeroes:
        min_zeroes = zeroes
        min_layer = layer[:]
print(min_layer.count('1') * min_layer.count('2'))

layers = [textwrap.wrap(layer, width) for layer in img]
for i in range(height):
    for j in range(width):
        current_layer = 0
        while layers[current_layer][i][j] == '2':
            current_layer += 1
        sys.stdout.write('1' if layers[current_layer][i][j] == '1' else ' ')
    print()
