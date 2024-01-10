from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def is_exit(x, y) -> bool:
            return (
                x in {0, len(maze) - 1}
                or y in {0, len(maze[0]) - 1}
            )
        
        def get_next_cells(x, y, step):
            next_cells = [
                (x + x_delta, y + y_delta)
                for x_delta, y_delta in (
                    (1, 0), (-1, 0), (0, 1), (0, -1),
                )
            ]
            return [
                ((x_prime, y_prime), step+1)
                for x_prime, y_prime in next_cells
                if (
                    0 <= x_prime < len(maze)
                    and 0 <= y_prime < len(maze[0])
                    and maze[x_prime][y_prime] == '.'
                )
            ]

        visited = set()
        q = deque([])
        start_node = (entrance[0], entrance[1]), 0
        q.append(start_node)
  
        while q:
            node, step = q.popleft()
            if node in visited: continue
            visited.add(node)
            if 0 < step and is_exit(*node):
                return step
            q += get_next_cells(*node, step)
        else:
            return -1

        return step
