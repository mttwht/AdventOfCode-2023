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
# # Example answer  = 374 with expansion of 2
# # Example answer  = 1030 with expansion of 10
# # Example answer  = 8410 with expansion of 100

EXPANSION_CONSTANT = 1000000


def find_galaxies(lines: list[str]) -> list[tuple[int, int]]:
    galaxies = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append((x, y))
    return galaxies


def expand_map(lines: list[str]) -> tuple[list[int], list[int]]:
    row_dists, col_dists = [], []
    
    for i, line in enumerate(lines):
        if line.count('#') == 0:
            row_dists.append(EXPANSION_CONSTANT)
        else:
            row_dists.append(1)
    
    for i in range(len(lines[0])):
        if [line[i] for line in lines].count('#') == 0:
            col_dists.append(EXPANSION_CONSTANT)
        else:
            col_dists.append(1)

    return row_dists, col_dists


def get_dist(p1: tuple[int, int], p2: tuple[int, int],
             row_dists: list[int], col_dists: list[int]) -> int:
    (x1, y1), (x2, y2) = p1, p2
    x_dist = sum(col_dists[min(x1, x2): max(x1, x2)])
    y_dist = sum(row_dists[min(y1, y2): max(y1, y2)])
    return x_dist + y_dist


row_dists, col_dists = expand_map(lines)
galaxies = find_galaxies(lines)

dists = []
for i, g1 in enumerate(galaxies):
    for j, g2 in enumerate(galaxies[i+1:]):
        dist = get_dist(g1, g2, row_dists, col_dists)
        dists.append(dist)
        print(g1, g2, dist)

print(sum(dists))
