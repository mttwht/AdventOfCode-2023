with open("input-01.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# """.splitlines()][1:]
# # Example answer  = 142

calibration_values = list()

for line in lines:
    first = None
    last = None
    for c in line:
        if c.isdigit():
            first = first or c
            last = c
    calibration_values.append(first + last)

answer = sum(int(v) for v in calibration_values)

print(answer)
