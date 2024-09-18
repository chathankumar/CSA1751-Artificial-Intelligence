
                           1.Write a python program to solve N queens’ problem 

Algorithm:

1.Initialize the Board: Create an empty board.
2.Place Queens: Try placing a queen in each column of the current row and check if it's safe.
3.Check Safety: Ensure that the current queen placement does not conflict with other queens.
4.Backtrack: If placing a queen leads to a solution, move to the next row. If not, backtrack and try the next position.
5.Output Solutions: Collect and display all valid solutions.

                           2.Write a python program to solve water jug problem
    
Algorithm:

Step 1: Initialize the BFS queue, visited set, and parent dictionary.
Step 2: Start BFS by dequeuing the current jug states.
Step 3: Check if the current state meets the target, and if so, trace the path back to the start.
Step 4: Generate all possible moves (fill, empty, transfer water between jugs).
Step 5: For each unvisited state, add it to the queue, mark it as visited, and store its parent for path tracing

                             3.Write a python program to solve Cript-Arthimetic problem

Algorithm:

1.	Identify Variables: Define the unique letters as variables to be mapped to digits (e.g., S, E, N, D, M, O, R, Y).
2.	Generate Permutations: Generate all possible digit assignments (0-9) for these letters while ensuring they are unique.
3.	Apply Constraints: Ensure that the first letter of each word (S and M) is not assigned the digit 0 (no leading zeros allowed).
4.	Formulate the Equation: Convert the words into numeric expressions using the digit assignments (SEND + MORE = MONEY).
5.	Check the Solution: Test each valid assignment to see if it satisfies the equation; return the correct assignment if found.


                             4.Write a python program to implement BFS.

Algorithm:

1.Initialize: Create a queue and enqueue the starting node. Mark it as visited.
2.Dequeue: Dequeue a node from the queue.
3.Process: Process the dequeued node (e.g., print or check).
4.Enqueue Neighbors: Enqueue all unvisited neighbors of the dequeued node and mark them as visited.
5.Repeat: Repeat steps 2-4 until the queue is empty. 
    

                               5.Write a python program to implement DFS.
    
ALGORITHM:

1.	Start at a node, mark it as visited.
2.	Visit the node and perform desired operation (e.g., print).
3.	For each unvisited adjacent node, recursively call DFS.
4.	Mark nodes visited during recursion.
5.	Continue until all nodes reachable from the start node are visited.


                               6.Write a python program to implement A*Search.
    
ALGORITHM:

1.	Initialize the open set with the start node and set its g-cost to 0.
2.	Pick the node with the lowest f-cost (g-cost + heuristic).
3.	If the current node is the goal, reconstruct the path and return it.
4.	For each neighbor, calculate tentative g-cost and update it if it's lower.
5.	Continue the process until the goal is reached or the open set is empty.
    

                               7.Write a python program to implement Map Colouring for attaining CSP

ALGORITHM:

1.	Define a function to check if a color assignment is valid.
2.	Use backtracking to try coloring each node with available colors.
3.	If a color assignment is valid, recursively try to color the next node.
4.	If a complete valid coloring is found, return the solution.
5.	If no valid coloring is possible, backtrack and try the next color.


                               8.Write a python program for implementing tic-tac-toe game.
ALGORITHM:

 1.	Initialize the game board and set players.
 2.	Loop through each turn to get player input and update the board.
 3.	Check for a win or draw after each move.
 4.	Display the board and prompt the next player.
 5.	End the game when there’s a winner or the board is full.


                              9.Write a python program to implement travelling sales man problem.
                              
ALGORITHM:

1.	List all cities and generate all possible routes (permutations).
2.	For each route, calculate the total cost (sum of edges between cities).
3.	Track the route with the lowest cost.
4.	Continue checking all permutations to find the optimal route.
5.	Return the route with the minimum cost once all routes are evaluated.







    

    




