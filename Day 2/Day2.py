# PART 1
with open('input.txt') as file:
    content = file.read()

ranges = content.split(',')
invalid = 0
for r in ranges:
    start = int(r.split('-')[0])
    end = int(r.split('-')[1])
    for num in range(start, end + 1):
        n = str(num)
        if len(n) % 2 == 0:
            if n[:len(n)//2] == n[len(n)//2:]:
                invalid += num
print(invalid)

# PART 2

def check_invalid(num):
    n = str(num)
    if len(n) == 1:
        return False
    for i in range(1, len(n)//2 + 1):
        if len(n) % i != 0:
            continue
        pattern = n[:i]
        if pattern * (len(n)//i) == n:
            return True
    return False

with open('input.txt') as file:
    content = file.read()

ranges = content.split(',')
invalid = set()
for r in ranges:
    start, end = map(int, r.split('-'))
    for num in range(start, end + 1):
        if check_invalid(num):
            #print(f"Invalid: {num}")
            invalid.add(num)
print(sum(invalid))
