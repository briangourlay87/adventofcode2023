import re

MAX_CUBES = {'red': 12,
             'green': 13,
             'blue': 14}

possible_games = 0
for line in open('day2/cubes.txt').read().splitlines():
    game_valid = True
    split_line = line.split(':')
    game_id, reveals = split_line[0].replace('Game ', ''), re.split('; |, ', split_line[1].lstrip(' '))
    for reveal in reveals:
        reveal_cubes, reveal_colour = reveal.split(' ')[0], reveal.split(' ')[1]
        if int(reveal_cubes) > MAX_CUBES.get(reveal_colour):
            game_valid = False
            break

    if game_valid:
        possible_games += int(game_id)

print('Number of possible games', possible_games)