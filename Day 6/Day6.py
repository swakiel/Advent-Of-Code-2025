# PART 1

from math import prod

with open('input.txt', 'r', encoding='utf-8') as f:
    matrix = [line.split() for line in f]

operations = matrix.pop()
cols = [[int(matrix[i][j]) for i in range(len(matrix))] for j in range(len(matrix[0]))]

total = 0
for i, operation in enumerate(operations):
    if operation == '+':
        total += sum(cols[i])
    else:
        total += prod(cols[i])
print(total)

# PART 2

with open('input.txt', 'r', encoding='utf-8') as f:
    matrix = [list(line.rstrip('\n')) for line in f]

operations = matrix.pop()
cols = [i for i, op in enumerate(operations) if op != ' ']

all_nums = []
for i in range(len(cols)-1):
    start = cols[i]
    end  = cols[i+1] - 1    # -1 to account for empty column txt file
    nums = []
    for j in range(start, end):
        num = ''
        for i in range(len(matrix)):
            num += matrix[i][j]
        num.replace(' ', '')
        nums.append(int(num))
    all_nums.append(nums)

start = cols[-1]
end  = len(matrix[0]) 
nums = []
for j in range(start, end):
    num = ''
    for i in range(len(matrix)):
        num += matrix[i][j]
    num.replace(' ', '')
    nums.append(int(num))
all_nums.append(nums)

operations = [op for op in operations if op != ' ']
total = 0
for i, operation in enumerate(operations):
    if operation == '+':
        total += sum(all_nums[i])
    else:
        total += prod(all_nums[i])
print(total)

