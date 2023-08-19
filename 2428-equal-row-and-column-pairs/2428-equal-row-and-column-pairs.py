from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(
            tuple(grid[i][j] for i in range(len(grid)))
            for j in range(len(grid))
        )
        cols = Counter(
            tuple(grid[j][i] for i in range(len(grid)))
            for j in range(len(grid))
        )
        return sum(
            rows[key] * cols[key]
            for key in rows.keys() & cols.keys()
        )
            
