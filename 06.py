# with open("input-06.txt", "r") as file:
#     lines = [line.strip() for line in file.readlines()]

lines = [line.strip() for line in """
Time:      7  15   30
Distance:  9  40  200
""".splitlines()][1:]
# Example answer  = 288


def parse_lines(lines: list[str]):
    times = [int(n) for n in lines[0].split(":")[1].split()]
    distances = [int(n) for n in lines[1].split(":")[1].split()]
    return times, distances


times, distances = parse_lines(lines)
winning_ways = []

for i in range(len(times)):
    ways = 0
    for duration in range(times[i]):
        if duration * (times[i] - duration) > distances[i]:
            ways += 1
    winning_ways.append(ways)

answer = 1
for w in winning_ways:
    answer *= w

print(answer)
