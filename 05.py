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
# # Example answer  = 46


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

for i in range(0, len(seeds), 2):
    seed = seeds[i]
    while seed < seeds[i] + seeds[i+1]:
        seed_val = seed
        min_dist_to_next_range = None
        for map in maps:
            map_val = None
            for map_range in map:
                if seed_val >= map_range[1] and seed_val < map_range[1] + map_range[2]:
                    diff = seed_val - map_range[1]
                    map_val = map_range[0] + diff
                    dist_to_next_range = map_range[2] - diff
                    if min_dist_to_next_range is None or dist_to_next_range < min_dist_to_next_range:
                        min_dist_to_next_range = dist_to_next_range
                    break
            if map_val is None:
                map_val = seed_val
                larger_min_diffs = [r[1] - seed_val for r in map if r[1] > seed_val]
                if len(larger_min_diffs) > 0:
                    if min_dist_to_next_range is None or min(larger_min_diffs) < min_dist_to_next_range:
                        min_dist_to_next_range = min(larger_min_diffs)
                # else:
                    # min_dist_to_next_range = 1
            seed_val = map_val
        locations.append(seed_val)

        # min_dist_to_next_range = max(1, min_dist_to_next_range)
        seed += min_dist_to_next_range
        # if min_dist_to_next_range > 1:
            # print(min_dist_to_next_range)

# print(locations)
print(min(locations))
