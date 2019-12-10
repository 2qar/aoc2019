import math
import sys

# y x flippy floppy

amap = open("input.txt").read().strip().split('\n')

def scan(pos: tuple) -> set:
    angles = set()

    for y in range(len(amap)):
        for x in range(len(amap)):
            if amap[x][y] == '#' and (x,y) != pos:
                angles.add(math.atan2(pos[1]-y,pos[0]-x))

    return len(angles)

max_asteroids = 0
max_point = None
for y in range(len(amap)):
    for x in range(len(amap)):
        if amap[x][y] == '#':
            asteroids = scan((x,y))
            if asteroids > max_asteroids:
                max_asteroids = asteroids
                max_point = (y,x)
print(f"Silver: {max_asteroids}")
