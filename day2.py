def read_instructions():
    with open('input/day2.csv', newline="") as f:
        line = f.read().strip()
        values = line.split(",")
    return values

def is_repeated_pattern(s: str) -> bool:
    return s in (s + s)[1:-1]


values = read_instructions()
total_sum = 0

for value in values:
    start, end = map(int, value.split("-"))
    for n in range(start, end + 1):
        if is_repeated_pattern(str(n)):
            total_sum += n

print(total_sum)
