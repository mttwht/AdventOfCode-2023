with open("input-09.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# lines = [line.strip() for line in """
# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
# """.splitlines()][1:]
# # Example answer  = 114

predictions = []
for line in lines:
    line_vals = []
    values = [int(n) for n in line.split()]
    line_vals.append(values)

    while values.count(0) != len(values):
        values = [values[i+1] - values[i] for i in range(len(values)-1)]
        line_vals.append(values)
    
    last_num = 0
    for diff_seq in reversed(line_vals):
        diff_seq.append(diff_seq[-1] + last_num)
        last_num = diff_seq[-1]
    
    predictions.append(last_num)

print(predictions)
print(sum(predictions))
