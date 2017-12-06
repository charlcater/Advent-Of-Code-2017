# Advent of Code 2017
# Day 03: Spiral Memory -- part 1

"""         33 
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8 3^2  10
21  22  23  24 5^2
..  ..  ..  ..  .. 7^2        
"""

import math 

input = 277678

# gives the vertical side length
def side_length(number):
    side = math.ceil(math.sqrt(number))
    side = side if side % 2 != 0 else side + 1
    # print('side = {}'.format(side))
    return side

# vertical steps
side = side_length(input)
vertical_steps = (side-1)/2 
# print('steps_to_central_axis: {}'.format(vertical_steps))

# horizontal steps
axes = [side**2 - ((side-1) * i)  - math.floor(side/2) for i in range(0, 4)]  # get the axis "cells"
# print(axes)
horisontal_steps = min([abs(axis - input) for axis in axes])

total_steps = int(horisontal_steps + vertical_steps)
print('Steps to reach {} = {}'.format(input, total_steps))
