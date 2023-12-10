with open("input-08.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)
# """.splitlines()][1:]
# # Example answer  = 2

# lines = [line.strip() for line in """
# LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)
# """.splitlines()][1:]
# # Example answer  = 6


def parse_nodes(lines):
    nodes = {}
    for line in lines:
        name, neighbours = [l.strip() for l in line.split("=")]
        neighbours = [l.strip() for l in neighbours[1:-1].split(",")]
        nodes[name] = neighbours
    return nodes

def parse_lines(lines):
    instructions = lines[0]
    nodes = parse_nodes(lines[2:])
    return instructions, nodes

START, END = "AAA", "ZZZ"

current_node = START

step_count = 0
instructions, nodes = parse_lines(lines)
while current_node != END:
    instruction = instructions[step_count % len(instructions)]
    if instruction == 'L':
        current_node = nodes[current_node][0]
    elif instruction == 'R':
        current_node = nodes[current_node][1]
    step_count += 1

print(step_count)
