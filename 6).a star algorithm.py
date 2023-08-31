print("k.mahesh 192110349")
import heapq

def a_star(grid, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in grid}
    g_score[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current[0] + neighbor[0], current[1] + neighbor[1]
            neighbor_node = (x, y)
            if neighbor_node in grid and not grid[neighbor_node]:
                tentative_g = g_score[current] + 1
                if tentative_g < g_score[neighbor_node]:
                    came_from[neighbor_node] = current
                    g_score[neighbor_node] = tentative_g
                    heapq.heappush(open_list, (tentative_g + abs(x - goal[0]) + abs(y - goal[1]), neighbor_node))

    return None
grid = {}
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    cells = list(map(int, input(f"Enter cells for row {i}: ").split()))
    for j, cell in enumerate(cells):
        grid[(i, j)] = cell

start = tuple(map(int, input("Enter start point: ").split()))
goal = tuple(map(int, input("Enter goal point: ").split()))

path = a_star(grid, start, goal)
print("Path found:", path) if path else print("No path found.")

