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


answer = 0

for i in range(len(lines)):
    line = lines[i]
    for match in re.finditer("\d+", line):
        neighbours = ""
        if i > 0:
            neighbours += lines[i-1][max(match.start()-1, 0):min(match.end()+1, len(line)-1)]
        if match.start() > 0:
            neighbours += line[match.start()-1]
        if match.end() < len(line)-1:
            neighbours += line[match.end()]
        if i < len(lines)-1:
            neighbours += lines[i+1][max(match.start()-1, 0):min(match.end()+1, len(line)-1)]
        
        if re.search("[^0-9.]", neighbours):
            num = int(match[0])
            answer += num

print(answer)
