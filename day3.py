def read_instructions():
    with open('input/day3.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]
    

def max_in_order(num_str, k):
    stack = []
    to_remove = len(num_str) - k
    for digit in num_str:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    return ''.join(stack[:k])


inputs = read_instructions()
total = 0
for num in inputs:
    num_str = str(num)
    largest_12 = int(max_in_order(num_str, 12))
    total += largest_12
print("Total output joltage:", total)