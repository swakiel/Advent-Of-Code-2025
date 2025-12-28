# PART 1
file_path = 'input.txt'
file = open(file_path)
new_file = file.read().replace('R', '').replace('L', '-')
file.close()

lines = new_file.splitlines()
current = 50
count = 0
for line in lines:
    current += int(line)
    current %= 100
    if current == 0:
        count += 1
print(count)

# PART 2
current = 50
count = 0
for line in lines:
    new = current + int(line)
    count += abs(new // 100)     # count how often 0 is crossed
    new %= 100
    if new == 0 and int(line) < 0:
        count += 1
    if current == 0 and int(line) < 0:
        count -= 1
    current = new
print(count)

