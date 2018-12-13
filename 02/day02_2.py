from collections import Counter

with open('input') as f:
    lines = [l.strip() for l in f.readlines()]

for this_line in lines:
    for other_line in lines:
        differences = 0
        for i in range(len(this_line)):
            if this_line[i] != other_line[i]:
                differences += 1
                diff_i = i
        if differences == 1:
            print(diff_i, this_line, other_line)
            line = this_line[0:diff_i] + this_line[diff_i+1:]
            print(line)
            print(''.join(set(line)))