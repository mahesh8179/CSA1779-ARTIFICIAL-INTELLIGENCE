from collections import deque

print("       k.mahesh 192110349")

def is_valid(s):
    m, c, b = s
    return (m == 0 or m >= c) and (3 - m == 0 or 3 - m >= 3 - c)

def next_states(s):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    valid_moves = []
    for move in moves:
        new_s = (s[0] - move[0], s[1] - move[1], 1 - s[2]) if s[2] == 1 else (s[0] + move[0], s[1] + move[1], 1 - s[2])
        if all(0 <= x <= 3 for x in new_s) and is_valid(new_s):
            valid_moves.append(new_s)
    return valid_moves

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    visited = set()
    q = deque([(start, [])])

    while q:
        s, path = q.popleft()
        if s == goal:
            return path

        if s not in visited:
            visited.add(s)
            for ns in next_states(s):
                q.append((ns, path + [s]))

    return None

solution = bfs()

if solution:
    for i, s in enumerate(solution):
        print(f"Step {i + 1}: Missionaries: {s[0]}, Cannibals: {s[1]}, Boat: {'Left' if s[2] == 1 else 'Right'}")
        if(i==10):
            print(f"Step {i + 2}: Missionaries: 0, Cannibals: 0, Boat: {'Left' if s[2] == 0 else 'Right'}")
            
else:
    print("No solution found.")
