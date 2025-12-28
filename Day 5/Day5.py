# PART 1

with open('input.txt') as file:
    lines = file.read().splitlines()

ranges = []
tests = []
switch = False

for line in lines:
    if line == '':
        switch = True
        continue
    if switch:
        tests.append(int(line))
    else:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

count = 0
for ingredient in tests:
    for start, end in ranges:
        if start <= ingredient <= end:
            count += 1
            break
print(count)

# PART 2

ranges.sort(key=lambda x: x[0])      # sort range by starting values
merged_ranges = []
current = ranges[0]
for r in ranges:
    if r[0] <= current[1]:
        current = min(current[0], r[0]), max(current[1], r[1])  # merging current and r
    else:
        merged_ranges.append(current)
        current = r
merged_ranges.append(current)

total = 0
for mr in merged_ranges:
    total += mr[1] - mr[0] + 1

print(total)

