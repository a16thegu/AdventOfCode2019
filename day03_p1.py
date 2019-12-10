# --- Day 3: Crossed Wires ---
# The gravity assist was successful, and you're well on your way to the Venus refuelling station. 
# During the rush back on Earth, the fuel management system wasn't completely installed, so that's
# next on the priority list.

# Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a 
# central port and extend outward on a grid. You trace the path each wire takes as it leaves the 
# central port, one wire per line of text (your puzzle input).

# The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you 
# need to find the intersection point closest to the central port. Because the wires are on a grid, 
# use the Manhattan distance for this measurement. While the wires do technically cross right at the
# central port where they both start, this point does not count, nor does a wire count as crossing 
# with itself.

# For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it 
# goes right 8, up 5, left 5, and finally down 3:

# ...........
# ...........
# ...........
# ....+----+.
# ....|....|.
# ....|....|.
# ....|....|.
# .........|.
# .o-------+.
# ...........
# Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

# ...........
# .+-----+...
# .|.....|...
# .|..+--X-+.
# .|..|..|.|.
# .|.-X--+.|.
# .|..|....|.
# .|.......|.
# .o-------+.
# ...........
# These wires cross at two locations (marked X), but the lower-left one is closer to the central 
# port: its distance is 3 + 3 = 6.

# Here are a few more examples:

# R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
# R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
# U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

# What is the Manhattan distance from the central port to the closest intersection?

import re

def splitInput(wirePath) :
    wire = []
    for path in wirePath :
        match = re.match(r"([a-z]+)([0-9]+)", path, re.I)
        if match:
            items = match.groups()
            wire.append(items)

    return wire

def addWirePosition(path) :
    wirePos = [(0, 0)]
    index = 0
    for pair in path :
        if pair[0] == 'U' :
            wirePos.append((wirePos[index][0], wirePos[index][1] + int(pair[1])))
            index += 1
        elif pair[0] == 'R' :
            wirePos.append((wirePos[index][0] + int(pair[1]), wirePos[index][1]))
            index += 1
        elif pair[0] == 'D' :
            wirePos.append((wirePos[index][0], wirePos[index][1] - int(pair[1])))
            index += 1
        elif pair[0] == 'L' :
            wirePos.append((wirePos[index][0] - int(pair[1]), wirePos[index][1]))
            index += 1

    return wirePos

fname = "input_day03.txt"
fh = open(fname)

#for line in fh :

testWire1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
testWire2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

wire1 = splitInput(testWire1)
wire2 = splitInput(testWire2)

posWire1 = addWirePosition(wire1)
posWire2 = addWirePosition(wire2)

print(posWire1)
print(posWire2)


# For calculating Manhattan Distance: https://www.geeksforgeeks.org/sum-manhattan-distances-pairs-points/