current = 50
zeros = 0

def read_instructions():
    with open('input/day1.txt', "r") as f:
        return f.read().strip().splitlines()
    

def process_instruction(instruction, current_position, zero_count):
    direction = instruction[0]
    steps = int(instruction[1:])

    if direction == "R":
        for _ in range(steps):
            current_position = (current_position + 1) % 100
            if current_position == 0:
                zero_count += 1

    elif direction == "L":
        for _ in range(steps):
            current_position = (current_position - 1) % 100
            if current_position == 0:
                zero_count += 1

    return current_position, zero_count

instructions = read_instructions()
for instruction in instructions:
    current, zeros = process_instruction(instruction, current, zeros)

print(f"Combo: {zeros}")