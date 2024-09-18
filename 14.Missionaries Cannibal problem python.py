from collections import deque
class MissionariesAndCannibals:
    def __init__(self):
        self.start_state = (3, 3, 1)  
        self.goal_state = (0, 0, 0)   
        self.explored = set()
    def is_valid(self, state):
        m_left, c_left, boat = state
        m_right, c_right = 3 - m_left, 3 - c_left
        if m_left >= 0 and m_right >= 0 and c_left >= 0 and c_right >= 0:
            if (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right):
                return True
        return False
    def get_successors(self, state):
        m_left, c_left, boat = state
        successors = []
        if boat == 1:  
            for m, c in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:  
                new_state = (m_left - m, c_left - c, 0)
                if self.is_valid(new_state):
                    successors.append(new_state)
        else:  
            for m, c in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
                new_state = (m_left + m, c_left + c, 1)
                if self.is_valid(new_state):
                    successors.append(new_state)
        return successors
    def bfs(self):
        queue = deque([(self.start_state, [])])  
        self.explored.add(self.start_state)

        while queue:
            state, path = queue.popleft()
            if state == self.goal_state:
                return path + [self.goal_state]  
            for successor in self.get_successors(state):
                if successor not in self.explored:
                    self.explored.add(successor)
                    queue.append((successor, path + [state]))
        return None 
problem = MissionariesAndCannibals()
solution = problem.bfs()
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
