with open("input-04.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """.splitlines()][1:]
# # Example answer  = 30


card_counts = [1 for i in range(len(lines))]

for index in range(len(lines)):
    line = lines[index]
    card_points = 0
    card, numbers = line.split(":")
    card_num = card.split()[1]
    winning_numbers, card_numbers = [nums.split() for nums in numbers.split("|")]
    for num in card_numbers:
        if winning_numbers.count(num):
            card_points += 1
    for i in range(index+1, index+1+card_points):
        if i < len(card_counts):
            card_counts[i] += card_counts[index]

print(sum(val for val in card_counts))
