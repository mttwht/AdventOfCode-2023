import re

with open("input-06.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# Time:      7  15   30
# Distance:  9  40  200
# """.splitlines()][1:]
# # Example answer  = 71503


def parse_lines(lines: list[str]):
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    return time, distance


time, distance = parse_lines(lines)

ways = 0
for duration in range(time):
    if duration * (time - duration) > distance:
        ways += 1

print(ways)
