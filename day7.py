from collections import deque, defaultdict

def read_instructions():
    with open('input/day7.txt', "r") as f:
        return f.read().rstrip('\n')
    

def build_graph(grid, start):
    R = len(grid)
    C = len(grid[0])
    graph = defaultdict(list)

    q = deque([start])
    visited = set()

    while q:
        r, c = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        nr = r + 1
        while nr < R and grid[nr][c] == '.':
            nr += 1

        if nr >= R:
            continue

        if grid[nr][c] == '^':
            for dc in (-1, 1):
                nc = c + dc
                if 0 <= nc < C:
                    graph[(r, c)].append((nr, nc))
                    q.append((nr, nc))
    return graph


def count_paths(graph, start):
    indeg = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indeg[v] += 1
    reachable = set(graph.keys())
    for vals in graph.values():
        reachable |= set(vals)

    paths = defaultdict(int)
    paths[start] = 1

    q = deque([node for node in reachable if indeg[node] == 0])

    while q:
        u = q.popleft()
        for v in graph[u]:
            paths[v] += paths[u]
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    total = 0
    for node in reachable:
        if node not in graph or len(graph[node]) == 0:
            total += paths[node]

    return total


instructions = read_instructions()
grid = [list(line) for line in instructions.splitlines()]
R = len(grid)
C = len(grid[0])

start = None
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            start = (r, c)
            break
    if start:
        break
if start is None:
    raise ValueError("Start position 'S' not found in the grid.")


graph = build_graph(grid, start)
print("Total unique paths from 'S' to bottom:", count_paths(graph, start))