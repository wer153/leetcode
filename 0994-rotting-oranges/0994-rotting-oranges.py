class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def get_adjacent_oranges(rotten_oranges):
            adjacent_oranges = set()
            for i,j in rotten_oranges:
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    x, y = i+dx, j+dy
                    if x in range(len(grid)) and y in range(len(grid[0])):
                        adjacent_oranges.add((x,y))
            return adjacent_oranges

        rotten_oranges = {
            (i,j) for i in range(len(grid)) for j in range(len(grid[0]))
            if grid[i][j] == 2
        }
        fresh_oranges = {
            (i,j) for i in range(len(grid)) for j in range(len(grid[0]))
            if grid[i][j] == 1
        }
        batch_count = 0

        while fresh_oranges:
            batch_count += 1
            rotting_oranges = fresh_oranges & get_adjacent_oranges(rotten_oranges)
            rotten_oranges |= rotting_oranges
            fresh_oranges -= rotting_oranges
            if not rotting_oranges:
                return -1
        return batch_count
 