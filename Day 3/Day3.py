# PART 1
with open('input.txt', 'r') as file:
    banks = file.read().splitlines()

total = 0
for bank in banks:
    first = bank[0]
    second = bank[-1]
    for i, num in enumerate(bank):
        if i == len(bank) - 1 or i == 0:
            continue
        if num > first:
            first = num
            second = bank[-1]
        elif num > second:
            second = num
    max_joltage = first + second
    total += int(max_joltage)
print(total)

# PART 2

total = 0
for bank in banks:
    top_12 = []
    remaining = len(bank)

    for num in bank:
        while top_12 and num > top_12[-1] and len(top_12) + remaining > 12:
            top_12.pop()
        if len(top_12) < 12:
            top_12.append(num)
        remaining -= 1

    max_joltage = ''.join(top_12)
    total += int(max_joltage)
print(total)
