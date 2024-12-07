reports = []

with open("input/day2") as f:
    for l in f:
        reports.append(list(map(int, l.split())))

def is_safe(levels): 
    deltas = [a-b for a,b in zip(levels, levels[1:])] # "borrowed" some of this from reddit
    return all(-3 <= n <=-1 for n in deltas) or all(1 <= n <= 3 for n in deltas)

part_a, part_b = 0, 0

for level in reports:
        part_a += is_safe(level)
        part_b += any(is_safe(level[:i]+level[i+1:]) for i in range(len(level)))

print(part_a,part_b)