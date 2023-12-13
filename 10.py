with open("input-10.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# ...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........
# """.splitlines()][1:]
# # Example answer  = 4

# lines = [line.strip() for line in """
# ..........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# ..........
# """.splitlines()][1:]
# # Example answer  = 4

# lines = [line.strip() for line in """
# .F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...
# """.splitlines()][1:]
# # Example answer  = 8

# lines = [line.strip() for line in """
# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# """.splitlines()][1:]
# # Example answer  = 10

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

just_pipe_map = [['.' for c in line] for line in lines]

dir = 'S'
pos = move(start_pos, dir)
pipe_len = 1

while pos != start_pos:
    (x, y) = pos
    pipe = lines[y][x]
    just_pipe_map[y][x] = pipe
    connections = CONNECTIONS[pipe]
    entry_dir = OPPOSITE_DIRECTION[dir]
    dir = [d for d in connections if d != entry_dir][0]
    pos = move(pos, dir)
    pipe_len += 1

entry_dir = OPPOSITE_DIRECTION[dir]
for c in CONNECTIONS:
    if entry_dir in CONNECTIONS[c] and 'S' in CONNECTIONS[c]:
        start_shape = c
        break
just_pipe_map[start_pos[1]][start_pos[0]] = start_shape

within_pipe_area = False
enclosed_tiles = 0
entry_piece = ''
for row in just_pipe_map:
    for tile in row:
        if tile == '|':
            within_pipe_area = not within_pipe_area
        elif tile in 'FL':
            entry_piece = tile
        elif tile in '7J':
            if entry_piece == 'F' and tile == 'J':
                within_pipe_area = not within_pipe_area
            elif entry_piece == 'L' and tile == '7':
                within_pipe_area = not within_pipe_area
        elif tile == '.' and within_pipe_area:
            enclosed_tiles += 1
print(enclosed_tiles)
