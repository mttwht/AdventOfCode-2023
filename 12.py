with open("input-12.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# """.splitlines()][1:]
# # Example answer  = 21


all_arrangements = []

def is_valid_arrangement(springs: str, counts: list[int]) -> bool:
    arrangement_counts = [len(s) for s in springs.replace('.', ' ').split()]
    return counts == arrangement_counts

def find_valid_arrangements(springs: str, counts: list[int]) -> int:
    if '?' in springs:
        valid_arrangements = 0
        valid_arrangements += find_valid_arrangements(springs.replace('?', '.', 1), counts)
        valid_arrangements += find_valid_arrangements(springs.replace('?', '#', 1), counts)
        return valid_arrangements
    else:
        if is_valid_arrangement(springs, counts):
            return 1
        else:
            return 0

for line in lines:
    print(line)
    springs, counts = line.split()
    counts = [int(s) for s in counts.split(',')]
    arrangements = find_valid_arrangements(springs, counts)
    all_arrangements.append(arrangements)
    print(arrangements)
    print()

print(sum(all_arrangements))