print("k.mahesh")
print("192110349")
print("CRIPT ARITHMETIC")
from itertools import permutations

def is_solution_valid(mapping):
    s = mapping['S']
    e = mapping['E']
    n = mapping['N']
    d = mapping['D']
    m = mapping['M']
    o = mapping['O']
    r = mapping['R']
    y = mapping['Y']
    
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    
    return send + more == money

def solve_cryptarithmetic():
    letters = set('SENDMORY')
    digits = range(10)
    
    for perm in permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))
        if is_solution_valid(mapping):
            return mapping
    
    return None

solution = solve_cryptarithmetic()

if solution:
    print("Cryptarithmetic Puzzle Solution:")
    for letter, digit in solution.items():
        print(f"{letter}: {digit}")
else:
    print("No solution found.")


