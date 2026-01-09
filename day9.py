

with open("input/day9.txt") as f:
    red = [tuple(map(int, line.strip().split(','))) for line in f]


edges = []
for i in range(len(red)):
    x1, y1 = red[i]
    x2, y2 = red[(i + 1) % len(red)]
    edges.append((x1, y1, x2, y2))

def intersects(minX, minY, maxX, maxY):
    for x1, y1, x2, y2 in edges:
        iMinX, iMaxX = min(x1, x2), max(x1, x2)
        iMinY, iMaxY = min(y1, y2), max(y1, y2)
        if minX < iMaxX and maxX > iMinX and minY < iMaxY and maxY > iMinY:
            return True
    return False

max_area = 0
for i in range(len(red)):
    for j in range(i+1, len(red)):
        x1, y1 = red[i]
        x2, y2 = red[j]
        minX, maxX = min(x1, x2), max(x1, x2)
        minY, maxY = min(y1, y2), max(y1, y2)
        
        manhattan = abs(x1 - x2) + abs(y1 - y2)
        if manhattan * manhattan > max_area:
            if not intersects(minX, minY, maxX, maxY):
                area = (maxX - minX + 1) * (maxY - minY + 1)
                if area > max_area:
                    max_area = area

print(max_area)