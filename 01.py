with open("input-01.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# """.splitlines()][1:]
# # Example answer  = 142

# # example for part 2
# lines = [line.strip() for line in """
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# """.splitlines()][1:]
# # Example answer  = 281

calibration_values = list()
number_words = "zero one two three four five six seven eight nine".split()

for line in lines:
    first = None
    last = None
    while len(line):
        if line[0].isdigit():
            first = first or line[0]
            last = line[0]
        else:
            for word in number_words[1:]:
                if line.startswith(word):
                    number = number_words.index(word)
                    first = first or str(number)
                    last = str(number)
                    break
        line = line[1:]
    calibration_values.append(first + last)

answer = sum(int(v) for v in calibration_values)

print(answer)
