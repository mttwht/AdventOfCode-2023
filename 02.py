import re

with open("input-02.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """.splitlines()][1:]
# # Example answer  = 2286


answer = 0

for line in lines:
    match = re.match("^Game (\d+): (.+)$", line)
    game_id, game = match.groups()
    mins = {
        'red': 1,
        'green': 1,
        'blue': 1
    }
    for reveal in game.split('; '):
        for colour_reveal in reveal.split(', '):
            qty, colour = colour_reveal.split()
            mins[colour] = max(mins[colour], int(qty))
    game_mins = mins['red'] * mins['green'] * mins['blue']
    # print(game_mins)
    answer += game_mins

print(answer)
