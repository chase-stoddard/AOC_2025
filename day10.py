from itertools import combinations
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def read_instructions():
    with open('input/day10.txt', "r") as f:
        return f.read().strip().splitlines()
    

def parse_button_as_int(s):
    res = 0
    for c in s[1:-1].split(","):
        res |= 1 << int(c)
    return res


def parse_button_as_list(s):
    return list(map(int, s[1:-1].split(",")))


def parse_diagram_as_int(s):
    res = 0
    for i, c in enumerate(s[1:-1]):
        if c == "#":
            res |= 1 << i
    return res


def parse_joltage(s):
    return list(map(int, s[1:-1].split(",")))


def solve_part_1(machine):
    diagram, buttons_as_int, _, _ = machine
    for presses in range(1 + len(buttons_as_int)):
        for comb in combinations(buttons_as_int, presses):
            lights = 0
            for button in comb:
                lights ^= button
            if lights == diagram:
                return presses
            

def solve_part_2(machine):
    _, _, buttons_as_list, joltage = machine

    B = np.zeros((len(joltage), len(buttons_as_list)), dtype=int)
    for j, button in enumerate(buttons_as_list):
        for light in button:
            B[light, j] = 1

    J = np.array(joltage, dtype=float)
    n_vars = len(buttons_as_list)
    c = np.ones(n_vars, dtype=float)
    constraints = LinearConstraint(B, lb=J, ub=J)
    bounds = Bounds(lb=np.zeros(n_vars), ub=np.full(n_vars, np.inf))
    integrality = np.ones(n_vars, dtype=int)

    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
    if not result.success:
        raise ValueError("MILP solver failed")
    
    x = np.rint(result.x).astype(int)
    return sum(x)


values = read_instructions()
# values = ['[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}', 
#            '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}', 
#            '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}']


machines = []
for line in values:
    parts = line.split(" ")
    diagram = parse_diagram_as_int(parts[0])
    buttons_as_int = [parse_button_as_int(b) for b in parts[1:-1]]
    buttons_as_list = [parse_button_as_list(b) for b in parts[1:-1]]
    joltage = parse_joltage(parts[-1])
    machines.append((diagram, buttons_as_int, buttons_as_list, joltage))

# print(sum(map(solve_part_1, machines)))

print(sum(map(solve_part_2, machines)))