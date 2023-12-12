with open("input-10.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# -L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF
# """.splitlines()][1:]
# # Example answer  = 4

# lines = [line.strip() for line in """
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# """.splitlines()][1:]
# # Example answer  = 8

OPPOSITE_DIRECTION = {
    'N': 'S',
    'E': 'W',
    'S': 'N',
    'W': 'E',
}

CONNECTIONS = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'L': ['N', 'E'],
    'J': ['N', 'W'],
    '7': ['S', 'W'],
    'F': ['S', 'E'],
    '.': [],
    'S': [],
}


def find_s_pos(map: list[str]):
    y = map.index([s for s in map if 'S' in s][0])
    x = map[y].index('S')
    return (x, y)

def move(pos: tuple[int, int], direction: str):
    (x, y) = pos
    if direction == 'N':
        return (x, y-1)
    elif direction == 'E':
        return (x+1, y)
    elif direction == 'S':
        return (x, y+1)
    elif direction == 'W':
        return (x-1, y)

def find_pipe_length(pipe_map: list[str]):
    (sx, sy) = find_s_pos(pipe_map)


def find_shape_of_s(pipe_map: list[str]):
    (sx, sy) = find_s_pos(pipe_map)


start_pos = find_s_pos(lines)
print(start_pos)

dir = 'S'
pos = move(start_pos, dir)
steps = 1

while pos != start_pos:
    (x, y) = pos
    pipe = lines[y][x]
    connections = CONNECTIONS[pipe]
    entry_dir = OPPOSITE_DIRECTION[dir]
    dir = [d for d in connections if d != entry_dir][0]
    pos = move(pos, dir)
    steps += 1

print(int(steps/2))
