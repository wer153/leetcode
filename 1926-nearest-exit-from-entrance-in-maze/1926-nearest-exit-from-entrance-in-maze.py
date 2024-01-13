from collections import deque
from itertools import chain

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x_range, y_range = range(len(maze)), range(len(maze[0]))
        
        def is_cell(x, y) -> bool:
            if x in x_range and y in y_range:
                if maze[x][y] == '.':
                    return True
            return False

        def is_exit(node) -> bool:
            x, y = node
            return is_cell(x, y) and any([
                x == x_range[0],
                x == x_range[-1],
                y == y_range[0],
                y == y_range[-1],
            ])

        def get_next_batch(batch):
            def get_neighbor_cells(x, y):
                return [
                    (x_prime, y_prime)
                    for x_prime, y_prime in ((x+1,y), (x-1,y), (x,y+1), (x,y-1))
                    if is_cell(x_prime, y_prime)
                ]
            next_batch = set()
            for cell in batch:
                for neighbor in get_neighbor_cells(*cell):
                    if neighbor not in visited:
                        next_batch.add(neighbor)
            return next_batch

        batch, visited, step = {tuple(entrance)}, set(), 0
        while batch:
            if 0 < step and any(filter(is_exit, batch)): return step
            step += 1
            visited |= batch
            batch = get_next_batch(batch)
        return -1