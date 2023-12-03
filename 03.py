import re

# with open("input-03.txt", "r") as file:
#     lines = [line.strip() for line in file.readlines()]

lines = [line.strip() for line in """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".splitlines()][1:]
# Example answer  = 4361

def add_num_to_gear(gears: dict[str, list[int]], gear_id: str, num: int) -> dict[str, list[int]]:
    if gear_id not in gears:
        gears[gear_id] = []
    gears[gear_id].append(num)
    return gears

def add_num_to_neighbouring_gears(gears: dict[str, list[int]], row: int, col: int, num: str) -> dict[str, list[int]]:
    line = lines[row]
    num_len = len(num)
    num = int(match[0])
    # check cells above
    if row > 0:
        for j in range(max(0, col - 1), min(len(line), col + num_len + 1)):
            if lines[row-1][j] == "*":
                add_num_to_gear(gears, str(row-1) + "-" + str(j), int(num))
    # check cell to left
    if col > 0:
        if lines[row][col - 1] == "*":
            add_num_to_gear(gears, str(row) + "-" + str(col - 1), int(num))
    # check cell to right
    if col + num_len < len(line)-1:
        if lines[row][col + num_len] == "*":
            add_num_to_gear(gears, str(row) + "-" + str(col + num_len), int(num))
    # check cells below
    if row < len(lines)-1:
        for j in range(max(0, col - 1), min(len(line), col + num_len + 1)):
            if lines[row+1][j] == "*":
                add_num_to_gear(gears, str(row+1) + "-" + str(j), int(num))
    return gears


gears = {}

answer = 0

for i in range(len(lines)):
    line = lines[i]
    for match in re.finditer("\d+", line):
        gears = add_num_to_neighbouring_gears(gears, i, match.start(), match[0])

for gear_id in gears:
    gear = gears[gear_id]
    # print(gear_id, gear)
    if len(gear) == 2:
        # print(gear[0], "*", gear[1], "=", gear[0] * gear[1])
        answer += gear[0] * gear[1]

print(answer)
