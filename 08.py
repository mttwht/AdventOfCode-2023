import math


with open("input-08.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
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



step_count = 0
instructions, nodes = parse_lines(lines)
current_nodes = [n for n in nodes if n.endswith("A")]
end_steps = [[] for n in current_nodes]
stop = False

while len([n for n in current_nodes if n.endswith("Z")]) < len(current_nodes):
    instruction = instructions[step_count % len(instructions)]
    if instruction == 'L':
        current_nodes = [nodes[n][0] for n in current_nodes]
    elif instruction == 'R':
        current_nodes = [nodes[n][1] for n in current_nodes]
    step_count += 1

    for i, n in enumerate(current_nodes):
        if n.endswith('Z'):
            end_steps[i].append(step_count)
            if min([len(s) for s in end_steps]) >= 1:
                stop = True
                break
    if stop:
        break

print(math.lcm(*[es[0] for es in end_steps]))
