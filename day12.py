def read_instructions():
    blocks = {}
    layouts = []
    current_id = None
    current_grid = []

    with open('input/day12.txt') as f:
        for line in f:
            stripped = line.strip()

            if stripped.endswith(":") and stripped[:-1].isdigit():
                if current_id is not None:
                    blocks[current_id] = current_grid
                current_id = int(stripped[:-1])
                current_grid = []
                continue

            if "x" in stripped and ":" in stripped and not stripped[:-1].isdigit():
                dims, rest = stripped.split(":")
                w, h = map(int, dims.split("x"))
                nums = list(map(int, rest.split()))
                layouts.append((w, h, nums))
                continue

            if stripped != "":
                current_grid.append(stripped)

    if current_id is not None:
        blocks[current_id] = current_grid

    return blocks, layouts


def block_area(block):
    return sum(row.count('#') for row in block)

def layout_area(layout):
    w, h, _ = layout
    return w * h

def blocks_sum(layout, blocks):
    _, _, counts = layout
    total = 0
    for block_id, count in enumerate(counts):
        total += count * block_area(blocks[block_id])

    return total


# blocks =   {0: ['###', '##.', '##.'], 1: ['###', '##.', '.##'], 2: ['.##', '###', '##.'], 3: ['##.', '###', '##.'], 4: ['###', '#..', '###'], 5: ['###', '.#.', '###']} 
# layouts = [(4, 4, [0, 0, 0, 0, 2, 0]), (12, 5, [1, 0, 1, 0, 2, 2]), (12, 5, [1, 0, 1, 0, 3, 2])]
    
total = 0

blocks, layouts = read_instructions()

for layout in layouts:
    layout_area_value = layout_area(layout)
    blocks_sum_value = blocks_sum(layout, blocks)
    if layout_area_value >= blocks_sum_value:
        total += 1

print(total)

