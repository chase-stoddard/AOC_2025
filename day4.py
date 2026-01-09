def read_instructions():
    with open('input/day4.txt', "r") as f:
        return f.read().strip().splitlines()
    

grid = [list(row) for row in read_instructions()]

rows = len(grid)
cols = len(grid[0])

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0), (1, 1)]

result = [[0] * cols for _ in range(rows)]

total_removed = 0

def count_adjacent(r, c):
    count = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                count += 1
    return count

def mark_cells():
    to_mark= []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_adjacent(r, c) < 4:
                    to_mark.append((r, c))

    for r, c in to_mark:
        grid[r][c] = 'x'

    return len(to_mark)


while True:
    removed = mark_cells()
    if removed == 0:
        break
    total_removed += removed

print(total_removed)