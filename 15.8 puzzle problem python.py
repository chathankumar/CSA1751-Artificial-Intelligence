import heapq
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  
def find_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance
def generate_successors(state):
    x, y = find_blank_position(state)
    successors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            successors.append(new_state)
    return successors
def astar(start_state):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state), 0, start_state, []))
    closed_list = set()

    while open_list:
        _, cost, current_state, path = heapq.heappop(open_list)

        if current_state == GOAL_STATE:
            return path + [current_state]

        closed_list.add(tuple(map(tuple, current_state)))

        for successor in generate_successors(current_state):
            if tuple(map(tuple, successor)) not in closed_list:
                new_cost = cost + 1
                heapq.heappush(open_list, (new_cost + manhattan_distance(successor), new_cost, successor, path + [current_state]))

    return None 
def print_puzzle(state):
    for row in state:
        print(row)
    print()
initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [7, 8, 6]]  
solution = astar(initial_state)
if solution:
    print("Solution found in {} steps:".format(len(solution)))
    for step in solution:
        print_puzzle(step)
else:
    print("No solution found.")
