import math
import itertools

def read_instructions():
    points = []
    with open("input/day8.txt", "r") as f:
        for line in f:
            x, y, z = map(float, line.strip().split(','))
            points.append((x, y, z))
    return points

def create_boxes(pairs):
    boxes = []

    for a, b in pairs:
        related_boxes = [box for box in boxes if a in box or b in box]

        if not related_boxes:
            boxes.append([a, b])
        else:
            new_box = set([a, b])
            for box in related_boxes:
                new_box.update(box)
                boxes.remove(box)
            boxes.append(list(new_box))

    return boxes


def find_box_index(boxes, point):
    for i, box in enumerate(boxes):
        if point in box:
            return i
    return None


def connect_boxes(boxes, sorted_pairs):
    last_connected = None

    for a, b in sorted_pairs:
        box_a = find_box_index(boxes, a)
        box_b = find_box_index(boxes, b)

        if box_a == box_b:
            continue

        boxes[box_a].extend(boxes[box_b])
        del boxes[box_b]

        last_connected = (a, b)

        if len(boxes) == 1:
            break

    return boxes, last_connected


values = read_instructions()
all_pairs = []
for a, b in itertools.combinations(values, 2):
    d = math.dist(a, b)
    all_pairs.append((a, b, d))

all_pairs_sorted = sorted(all_pairs, key=lambda x: x[2])

closest_n = 1000
closest_pairs = [(a, b) for a, b, _ in all_pairs_sorted[:closest_n]]

boxes = create_boxes(closest_pairs)

in_boxes = set(p for box in boxes for p in box)
for p in values:
    if p not in in_boxes:
        boxes.append([p])

remaining_pairs = [(a, b) for a, b, _ in all_pairs_sorted[closest_n:]]
boxes, last_pair = connect_boxes(boxes, remaining_pairs)

(a_last, b_last) = last_pair
result = a_last[0] * b_last[0]

print("Last connected points:", a_last, b_last)
print("X-coordinate product:", result)

# box_sizes = sorted([len(box) for box in boxes], reverse=True)
# top_3_sizes = box_sizes[:3]

# print("Sizes of three largest circuits:", top_3_sizes)

# total = 1
# for size in top_3_sizes:
#     total *= size

# print("Product of sizes:", total)


