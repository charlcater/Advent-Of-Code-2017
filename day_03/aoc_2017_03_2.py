# Advent of Code 2017
# Day 03: Spiral Memory -- part 2
# Not my solution, but a very elegant way to solve
  
'''
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
'''

from itertools import count

input = 277678

def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2)
                                             for l in range(j-1,j+2))
                yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n:
        	# print('First value larger than input: {}'.format(x))
        	return x

print(part2(input))
