from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x_range, y_range = range(len(maze)), range(len(maze[0]))
        
        def is_exit(x, y) -> bool:
            return any([
                x == x_range[0],
                x == x_range[-1],
                y == y_range[0],
                y == y_range[-1],
            ])
        
        def get_neighbor_cells(x, y):
            return [
                (x_prime, y_prime)
                for x_prime, y_prime in (
                    (x+1,y), (x-1,y), (x,y+1), (x,y-1)
                )
                if (
                    x_prime in x_range
                    and y_prime in y_range
                    and maze[x_prime][y_prime] == '.'
                )
            ]

        visited = set()
        q = deque([(tuple(entrance), 0)])
  
        while q:
            node, step = q.popleft()
            if node in visited: continue
            visited.add(node)
            if 0 < step and is_exit(*node):
                return step
            q += [(cell, step+1) for cell in get_neighbor_cells(*node)]
        else:
            return -1

        return step
