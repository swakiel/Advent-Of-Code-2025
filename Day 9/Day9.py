# PART 1

with open('input.txt', 'r', encoding='utf-8') as f:
    grid = [[int(num) for num in line.rstrip('\n').split(',')] for line in f]

best = 0
for i in range(len(grid) - 1):
    for j in range(i, len(grid)):
        x1, y1 = grid[i]
        x2, y2 = grid[j]
        area = (abs(x1 - x2) +1)* (abs(y1 - y2) + 1)
        best = max(best, area)
print(best)

# PART 2

from collections import deque

rows = max([point[0] for point in grid])
columns = max([point[1] for point in grid])
floor = [['.'] * columns for _ in range(rows)]

# create floor with boundaries
last = grid[-1]
for r, c in grid:
    floor[r-1][c-1] = '#'

    if last[0] == r:
        start = min(last[1], c)
        end = max(last[1]-1, c-1)
        floor[r-1][start : end] = ['—'] * (end - start)
    else:
        start = min(last[0], r)
        end = max(last[0]-1, r-1)
        for row in range(start, end):
            floor[row][c-1] = '|'
    last = [r, c]

print("Boundary created")
#for row in floor:
#    print(row)

# pad grid with layer of '.'
R, C = len(floor), len(floor[0])
padded = [['.'] * (C + 2)]
for row in floor:
    padded.append(['.'] + row + ['.'])
padded.append(['.'] * (C + 2))


# BFS to compute all points outside the boundary
R, C = len(padded), len(padded[0])
outside = [[0] * C for _ in range(R)]
q = deque([(0, 0)])
outside[0][0] = 1

while q:
    r, c = q.popleft()
    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and not outside[nr][nc]:
            if padded[nr][nc] == '.':   # only move through empty space
                outside[nr][nc] = 1
                q.append((nr, nc))

# remove padding
for i, row in enumerate(outside):
    outside[i] = row[1:-1]

outside.pop(0)
outside.pop()

print("Outside created")

#print("Outside matrix: \n")
#for row in outside:
#    print(row)


def legal(corner1, corner2, outside):
    x1, y1 = corner1
    x2, y2 = corner2  

    r1, r2 = sorted((x1, x2))
    c1, c2 = sorted((y1, y2))

    for r in range(r1-1, r2):
        for c in range(c1-1, c2):
            if outside[r][c] == 1:
                return False
    return True



best = 0
for i in range(len(grid) - 1):
    for j in range(i+1, len(grid)):
        if legal(grid[i], grid[j], outside):
            x1, y1 = grid[i]
            x2, y2 = grid[j]
            area = (abs(x1 - x2) +1)* (abs(y1 - y2) + 1)
            best = max(best, area)
print(best)
