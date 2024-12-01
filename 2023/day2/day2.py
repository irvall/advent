import sys

use_test_data = not False
lines = [line.rstrip('\n') for line in open('mini.txt' if use_test_data else 'input.txt')]

""" Puzzle input sneak peek:
Game 1: 9 red, 5 blue, 6 green; 6 red, 13 blue; 2
"""

def part_one():
    possible_games = []
    for line in lines:
        game, cubes = line.split(':')
        game_id = int(game.split()[-1])
        game_possible = True
        for subset in cubes.split(';'):
            tr, tg, tb = 12, 13, 14
            for cube in subset.split(','):
                count, color = cube.split()
                count = int(count)
                match color:
                    case 'red': tr -= count
                    case 'green': tg -= count
                    case 'blue': tb -= count
            if tr < 0 or tg < 0 or tb < 0:
                game_possible = False
                break
        if game_possible:
            possible_games.append(game_id)
    return sum(possible_games)

def part_two():
    ans = 0
    powers = []
    for line in lines:
        tr, tg, tb = 0, 0, 0
        game, cubes = line.split(':')
        for subset in cubes.split(';'):
            for cube in subset.split(','):
                count, color = cube.split()
                count = int(count)
                match color:
                    case 'red': tr = max(tr, count)
                    case 'green': tg = max(tg, count)
                    case 'blue': tb = max(tb, count)
        powers.append(tr*tg*tb)
    return sum(powers)



if __name__ == '__main__':
    p1, p2 = part_one(), part_two()
    if p1: print('part one:', p1)
    if p2: print('part two:', p2)
