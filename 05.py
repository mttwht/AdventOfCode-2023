with open("input-05.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4
# """.splitlines()][1:]
# # Example answer  = 35


def parse(lines: list[str]):
    maps = []
    for line in lines:
        if line.startswith("seeds:"):
            seeds = [int(n) for n in line.split(":")[1].split()]
        elif line.endswith("map:"):
            map_name, _ = line.split()
            map = []
            maps.append(map)
        elif len(line) == 0:
            continue
        elif line[0].isnumeric():
            map.append(tuple(int(n) for n in line.split()))
    return seeds, maps


seeds, maps = parse(lines)
locations = []

for seed in seeds:
    seed_val = seed
    for map in maps:
        map_val = None
        for range in map:
            if seed_val >= range[1] and seed_val < range[1] + range[2]:
                diff = seed_val - range[1]
                map_val = range[0] + diff
                break
        if map_val is None:
            map_val = seed_val
        seed_val = map_val
    locations.append(seed_val)

print(locations)
print(min(locations))
