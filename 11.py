with open("input-11.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# """.splitlines()][1:]
# # Example answer  = 374


def find_galaxies(lines: list[str]) -> list[tuple[int, int]]:
    galaxies = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append((x, y))
    return galaxies

def expand_map(lines: list[str]) -> list[str]:
    i = 0
    while i < len(lines):
        if lines[i].count('#') == 0:
            lines.insert(i, ''.join('.' for c in lines[i]))
            i += 1
        i += 1
    i = 0
    while i < len(lines[0]):
        if [line[i] for line in lines].count('#') == 0:
            lines = [line[:i] + '.' + line[i:] for line in lines]
            i += 1
        i += 1    
    return lines

def get_dist(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    (x1, y1), (x2, y2) = p1, p2
    return abs(x1-x2) + abs(y1-y2)


lines = expand_map(lines)
galaxies = find_galaxies(lines)

dists = []
for i, g1 in enumerate(galaxies):
    for j, g2 in enumerate(galaxies[i+1:]):
        dist = get_dist(g1, g2)
        dists.append(dist)
        print(g1, g2, dist)

print(sum(dists))
