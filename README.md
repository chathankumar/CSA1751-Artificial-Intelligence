
                     1.Write a python program to solve N queens’ problem 

Algorithm:

1.  Initialize the Board: Create an empty board.
2.Place Queens: Try placing a queen in each column of the current row and check if it's safe.
3.Check Safety: Ensure that the current queen placement does not conflict with other queens.
4.Backtrack: If placing a queen leads to a solution, move to the next row. If not, backtrack and try the next position.
5.Output Solutions: Collect and display all valid solutions.

Code:

def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True

    def solve(board, col):
        if col >= n:
            result.append([''.join(row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                solve(board, col + 1)
                board[i][col] = '.'

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return result
n = 4
solutions = solve_n_queens(n)
for sol in solutions:
    for row in sol:
        print(row)
    print()
    

                          2.Write a python program to solve water jug problem
    
Algorithm:

Step 1: Initialize the BFS queue, visited set, and parent dictionary.
Step 2: Start BFS by dequeuing the current jug states.
Step 3: Check if the current state meets the target, and if so, trace the path back to the start.
Step 4: Generate all possible moves (fill, empty, transfer water between jugs).
Step 5: For each unvisited state, add it to the queue, mark it as visited, and store its parent for path tracing

Code:

from collections import deque
def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    queue, visited = deque([(0, 0)]), set((0, 0))
    while queue:
        jug1, jug2 = queue.popleft()
        if jug1 == target or jug2 == target:
            return f"Solution found: ({jug1}, {jug2})"
        moves = [
            (jug1_capacity, jug2), (jug1, jug2_capacity),(0, jug2), (jug1, 0),  
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   
        ]
        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return "No solution found."
print(water_jug_bfs(4, 3, 2))


                             3.Write a python program to solve Cript-Arthimetic problem

Algorithm:

1.	Identify Variables: Define the unique letters as variables to be mapped to digits (e.g., S, E, N, D, M, O, R, Y).
2.	Generate Permutations: Generate all possible digit assignments (0-9) for these letters while ensuring they are unique.
3.	Apply Constraints: Ensure that the first letter of each word (S and M) is not assigned the digit 0 (no leading zeros allowed).
4.	Formulate the Equation: Convert the words into numeric expressions using the digit assignments (SEND + MORE = MONEY).
5.	Check the Solution: Test each valid assignment to see if it satisfies the equation; return the correct assignment if found.

Code:

from itertools import permutations
def solve_cryptarithmetic():
    letters = 'SENDMORY'
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        send = mapping['S'] * 1000 + mapping['E'] * 100 + mapping['N'] * 10 + mapping['D']
        more = mapping['M'] * 1000 + mapping['O'] * 100 + mapping['R'] * 10 + mapping['E']
        money = mapping['M'] * 10000 + mapping['O'] * 1000 + mapping['N'] * 100 + mapping['E'] * 10 + mapping['Y']
        if send + more == money:
            print(f"Solution found: {mapping}")
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
solve_cryptarithmetic()



                             4.Write a python program to implement BFS.

Algorithm:

1.Initialize: Create a queue and enqueue the starting node. Mark it as visited.
2.Dequeue: Dequeue a node from the queue.
3.Process: Process the dequeued node (e.g., print or check).
4.Enqueue Neighbors: Enqueue all unvisited neighbors of the dequeued node and mark them as visited.
5.Repeat: Repeat steps 2-4 until the queue is empty. 

CODE:

from collections import deque
def bfs(graph, start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    traversal_order = []
    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal_order
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start_node = 'A'
    print("BFS Traversal Order:", bfs(graph, start_node))
    

                               5.Write a python program to implement DFS.
    
ALGORITHM:

1.	Start at a node, mark it as visited.
2.	Visit the node and perform desired operation (e.g., print).
3.	For each unvisited adjacent node, recursively call DFS.
4.	Mark nodes visited during recursion.
5.	Continue until all nodes reachable from the start node are visited.

CODE:

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],I - 
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start_node = 'A'
    print("DFS Traversal Order:", end=' ')
    dfs(graph, start_node)
    

                                  6.Write a python program to implement A*Search.
    
ALGORITHM:

1.	Initialize the open set with the start node and set its g-cost to 0.
2.	Pick the node with the lowest f-cost (g-cost + heuristic).
3.	If the current node is the goal, reconstruct the path and return it.
4.	For each neighbor, calculate tentative g-cost and update it if it's lower.
5.	Continue the process until the goal is reached or the open set is empty.

CODE:

from heapq import heappop, heappush
def a_star_search(graph, start, goal, h):
    open_set = [(0, start)]
    g_cost = {start: 0}
    came_from = {}
    while open_set:
        current = heappop(open_set)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for neighbor, cost in graph[current]:
            tentative_g = g_cost[current] + cost
            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + h(neighbor, goal)
                heappush(open_set, (f_cost, neighbor))
                came_from[neighbor] = current
    return None  
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
if __name__ == "__main__":
    graph = {
        (0, 0): [((1, 0), 1), ((0, 1), 1)],
        (1, 0): [((0, 0), 1), ((1, 1), 1)],
        (0, 1): [((0, 0), 1), ((1, 1), 1)],
        (1, 1): [((1, 0), 1), ((0, 1), 1), ((2, 2), 1)],
        (2, 2): [((1, 1), 1)]
    }
    start_node = (0, 0)
    goal_node = (2, 2)
    print("A* Search Path:", a_star_search(graph, start_node, goal_node, heuristic))
    

                                      7.Write a python program to implement Map Colouring for attaining CSP

ALGORITHM:

1.	Define a function to check if a color assignment is valid.
2.	Use backtracking to try coloring each node with available colors.
3.	If a color assignment is valid, recursively try to color the next node.
4.	If a complete valid coloring is found, return the solution.
5.	If no valid coloring is possible, backtrack and try the next color.

CODE:

def is_valid(graph, colors, node, color):
    return all(colors.get(nei) != color for nei in graph[node])
def map_coloring(graph, colors, nodes, index, color_list):
    if index == len(nodes):
        return True
    node = nodes[index]
    for color in color_list:
        if is_valid(graph, colors, node, color):
            colors[node] = color
            if map_coloring(graph, colors, nodes, index + 1, color_list):
                return True
            colors[node] = None
    return False
def solve_map_coloring(graph, color_list):
    colors = {node: None for node in graph}
    nodes = list(graph.keys())
    if map_coloring(graph, colors, nodes, 0, color_list):
        return colors
    return None
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['A', 'B', 'F'],
        'D': ['A', 'E'],
        'E': ['B', 'D', 'F'],
        'F': ['C', 'E']
    }
    color_list = ['Red', 'Green', 'Blue']
    solution = solve_map_coloring(graph, color_list)
    print("Map Coloring Solution:", solution)

                               8.Write a python program for implementing tic-tac-toe game.
ALGORITHM:

 1.	Initialize the game board and set players.
 2.	Loop through each turn to get player input and update the board.
 3.	Check for a win or draw after each move.
 4.	Display the board and prompt the next player.
 5.	End the game when there’s a winner or the board is full.

CODE:

def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()
def check_winner(board, player):
    return any(
        all(cell == player for cell in line)
        for line in (board, zip(*board), [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]])
    )

def tic_tac_toe():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    for turn in range(9):
        print_board(board)
        player = players[turn % 2]
        row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
        if board[row][col] == ' ':
            board[row][col] = player
        else:
            print("Cell occupied, try again.")
            continue
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return
    print_board(board)
    print("It's a draw!")
if __name__ == "__main__":
    tic_tac_toe()

                              9.Write a python program to implement travelling sales man problem.
                              
ALGORITHM:

1.	List all cities and generate all possible routes (permutations).
2.	For each route, calculate the total cost (sum of edges between cities).
3.	Track the route with the lowest cost.
4.	Continue checking all permutations to find the optimal route.
5.	Return the route with the minimum cost once all routes are evaluated.

CODE:

from itertools import permutations
def calculate_route_cost(graph, route):
    return sum(graph[route[i]][route[i+1]] for i in range(len(route)-1)) + graph[route[-1]][route[0]]
def tsp(graph):
    nodes = list(graph.keys())
    all_routes = permutations(nodes)
    min_cost = float('inf')
    best_route = None    
    for route in all_routes:
        cost = calculate_route_cost(graph, route)
        if cost < min_cost:
            min_cost = cost
            best_route = route
    return best_route, min_cost
if __name__ == "__main__":
    graph = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
    }
    best_route, min_cost = tsp(graph)
    print(f"Best route: {best_route}, Minimum cost: {min_cost}")





    

    




