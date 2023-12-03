import re

with open("input-03.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """.splitlines()][1:]
# # Example answer  = 4361

def add_num_to_gear(gears: dict[str, list[int]], gear_id: str, num: int) -> dict[str, list[int]]:
    if gear_id not in gears:
        gears[gear_id] = []
    gears[gear_id].append(num)
    return gears


gears = {}

answer = 0

for i in range(len(lines)):
    line = lines[i]
    for match in re.finditer("\d+", line):
        num = int(match[0])
        if i > 0:
            for j in range(max(0, match.start() - 1), min(len(line), match.end() + 1)):
                if lines[i-1][j] == "*":
                    add_num_to_gear(gears, str(i-1) + "-" + str(j), int(num))
        if match.start() > 0:
            if lines[i][match.start() - 1] == "*":
                add_num_to_gear(gears, str(i) + "-" + str(match.start() - 1), int(num))
        if match.end() < len(line)-1:
            if lines[i][match.end()] == "*":
                add_num_to_gear(gears, str(i) + "-" + str(match.end()), int(num))
        if i < len(lines)-1:
            for j in range(max(0, match.start() - 1), min(len(line), match.end() + 1)):
                if lines[i+1][j] == "*":
                    add_num_to_gear(gears, str(i+1) + "-" + str(j), int(num))

for gear_id in gears:
    gear = gears[gear_id]
    print(gear_id, gear)
    if len(gear) == 2:
        print(gear[0], "*", gear[1], "=", gear[0] * gear[1])
        answer += gear[0] * gear[1]

print(answer)
