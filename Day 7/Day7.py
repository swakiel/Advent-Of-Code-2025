# PART 1

with open('input.txt', 'r', encoding='utf-8') as f:
    matrix = [list(line.rstrip('\n')) for line in f]

splits_count = 0
beam_idx = {i for i, char in enumerate(matrix[0]) if char == 'S'}
for i, row in enumerate(matrix[1:]):
    new_beam_idx = set()
    for index in beam_idx:
        if row[index] == '^':
            splits_count += 1
            new_beam_idx.add(index - 1)
            new_beam_idx.add(index + 1)
        else:
            new_beam_idx.add(index)
    beam_idx = new_beam_idx
print(splits_count)


# PART 2
def solve_part2(grid):
    rows = len(grid)
    cols = len(grid[0])

    timelines = [[0] * cols for _ in range(rows)]

    for c in range(cols):
        if grid[0][c] == 'S':
            timelines[0][c] = 1

    for r in range(rows):
        for c in range(cols):
            t = timelines[r][c]
            if t == 0:
                continue

            cell = grid[r][c]

            if cell in ('.', 'S'):
                if r + 1 < rows:
                    timelines[r + 1][c] += t

            elif cell == '^':
                if r + 1 < rows:
                    if c - 1 >= 0:
                        timelines[r + 1][c - 1] += t
                    if c + 1 < cols:
                        timelines[r + 1][c + 1] += t

    # All timelines that reach the bottom row are final
    return sum(timelines[rows - 1])

print(solve_part2(matrix))