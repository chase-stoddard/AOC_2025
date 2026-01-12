def read_instructions():
    range_strings = []
    with open('input/day5.txt', "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            range_strings.append(line)
    return range_strings
    

# def parse_instructions(instructions):
#     ranges = []
#     ids = []
#     in_id_section = False

#     for instruction in instructions:
#         if instruction == "":
#             in_id_section = True
#             continue
        
#         if not in_id_section:
#             ranges.append(instruction)


#     return ranges


def parse_range(r):
    a, b = r.split("-")
    return int(a), int(b)


# def id_in_range(id, ranges):
#     for r in ranges:
#         low, high = parse_range(r)
#         if low <= id <= high:
#             return True
#     return False

def merge_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: (x[0], x[1]))
    merged = []
    for low, high in ranges:
        if not merged or low > merged[-1][1] + 1:
            merged.append([low, high])
        else:
            merged[-1][1] = max(merged[-1][1], high)
    return merged


def all_ids_in_ranges(range_strings):
    ranges = [parse_range(r) for r in range_strings]
    merged = merge_ranges(ranges)
    total = sum(high - low + 1 for low, high in merged)
    return merged, total


instructions = read_instructions()
merged, total = all_ids_in_ranges(instructions)

#print("Merged ranges:", merged)
print("Total unique IDs:", total)