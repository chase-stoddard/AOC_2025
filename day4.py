def read_instructions():
    with open("input/day4.txt") as f:
        lines = [line.rstrip("\n") for line in f]
    grid = [list(line) for line in lines]
    width = max(len(row) for row in grid)
    for row in grid:
        row.extend(" " * (width - len(row)))
    columns = list(zip(*grid))
    return columns


def split_problems(columns):
    problems = []
    current = []
    for col in reversed(columns):
        if all(c == " " for c in col):
            if current:
                problems.append(list(current))
                current = []
        else:
            current.append(col)
    if current:
        problems.append(list(current))
    return problems


def parse_problem(cols):
    digit_cols = [col for col in cols if not all(c == ' ' for c in col)]
    if not digit_cols:
        return [], None
    bottom_row = digit_cols[-1][-1]
    operator = bottom_row.strip()
    numbers = []
    for col in digit_cols:
        digits = col[:][:]
        digit_str = "".join(d for d in digits if d.isdigit())
        if digit_str:
            numbers.append(int(digit_str))
    print("Parsed numbers:", numbers, "operator:", operator, "digit_cols:", digit_cols)
    return numbers, operator


def perform_math(numbers, op):
    if op == '+':
        total = sum(numbers)
    elif op == '*':
        total = 1
        for n in numbers:
            total *= n
    else:
        print(f"Operator raw: '{op}'")
        raise ValueError("Bad operator")
    return total


columns = read_instructions()
problems = split_problems(columns)
grand_total = 0
for prob in problems:
    nums, op = parse_problem(prob)
    result = perform_math(nums, op)
    print(nums, op, "=", result)
    grand_total += result
print("Grand total =", grand_total)