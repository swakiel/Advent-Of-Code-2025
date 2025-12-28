# PART 1

with open('input.txt', 'r', encoding='utf-8') as f:
    matrix = [list(line.rstrip('\n')) for line in f]

n, m = len(matrix), len(matrix[0])
count = 0
for row in range(n):
    for col in range(m):
        if matrix[row][col] == '@':
            total = -1
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if 0 <= row + i < n and 0 <= col + j < m and matrix[row + i][col + j] == '@':
                        total += 1
            if total < 4:
                count += 1
print(count)

# PART 2

count = 0
change = True
while change:
    change = False
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == '@':
                total = -1
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 <= row + i < n and 0 <= col + j < m and matrix[row + i][col + j] == '@':
                            total += 1
                if total < 4:
                    matrix[row][col] = '.'
                    change = True
                    count += 1
print(f"Part 2: {count}")

