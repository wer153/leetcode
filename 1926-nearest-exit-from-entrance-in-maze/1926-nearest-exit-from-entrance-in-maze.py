from collections import deque
from itertools import chain

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
            for x_prime, y_prime in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if x_prime in x_range and y_prime in y_range:
                    if maze[x_prime][y_prime] == '.':
                        yield (x_prime, y_prime)

        visited = set()
        batch = {tuple(entrance)}
        step = 0
        while batch:
            if 0 < step and any([True for cell in batch if is_exit(*cell)]):
                return step
            step += 1
            visited |= batch
            batch = {
                cell
                for cell in set(chain.from_iterable(get_neighbor_cells(*cell) for cell in batch))
                if cell not in visited
            }
        else:
            return -1

        return step
