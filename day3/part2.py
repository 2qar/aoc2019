import operator
import sys

wires = [moves.split(",") for moves in open("input.txt").read().split("\n")[:-1]]

#test = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
#test = "R8,U5,L5,D3\nU7,R6,D4,L4"
#test = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
#wires = [moves.split(",") for moves in test.split("\n")]

segments = []

i = 0
lastpoint=[0,0,0]
for move in wires[0]:
    point = lastpoint[:]
    if move[0] == "R":
        point[0] += int(move[1:])
    elif move[0] == "L":
        point[0] -= int(move[1:])
    elif move[0] == "U":
        point[1] += int(move[1:])
    elif move[0] == "D":
        point[1] -= int(move[1:])
    point[2] += int(move[1:])
    segments.append([lastpoint[:],point[:]])
    lastpoint = point[:]
    i+=1

#print(segments)

def manhatten_distance(point1, point2):
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

def steps(point, start, end, axis):
    return end[2] - abs(end[axis] - point[axis])

def intersecting(point, start, end, axis):
    if start[not axis] == end[not axis] and point[not axis] == end[not axis]:
        if start[axis] <= end[axis]:
            return point[axis] >= start[axis] and point[axis] <= end[axis]
        return point[axis] <= start[axis] and point[axis] >= end[axis]
    return False

stp = []
def check_intersecting(point, move, idx, op):
    i = 0
    while i < int(move[1:]):
        for segment in segments:
            for axis in [0, 1]:
                if intersecting(point, segment[0], segment[1], axis):
                    #print(f"distance: {manhatten_distance((0,0),point)} point: {point} segment: {segment}")
                    stp.append(point[2] + steps(point, segment[0], segment[1], axis))
                        
        point[idx] = op(point[idx], 1)
        point[2] += 1
        i += 1

point = [0,0,0]
for move in wires[1]:
    if move[0] == "R":
        check_intersecting(point, move, 0, operator.add)
    elif move[0] == "L":
        check_intersecting(point, move, 0, operator.sub)
    elif move[0] == "U":
        check_intersecting(point, move, 1, operator.add)
    elif move[0] == "D":
        check_intersecting(point, move, 1, operator.sub)

minsteps = sys.maxsize
for step in stp:
    if step < minsteps and step > 0:
        minsteps = step
print(minsteps)
