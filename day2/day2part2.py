import math
import re

sum_power = 0
for line in open('day2/cubes.txt').read().splitlines():
    min_required = {'red': 0, 'blue': 0, 'green': 0}
    split_line = line.split(':')
    reveals = re.split('; |, ', split_line[1].lstrip(' '))
    for reveal in reveals:
        reveal_cubes, reveal_colour = reveal.split(' ')[0], reveal.split(' ')[1]
        if int(reveal_cubes) > min_required.get(reveal_colour):
            min_required[reveal_colour] = int(reveal_cubes)
    sum_power += math.prod(min_required.values())
print('Sum Power', sum_power)