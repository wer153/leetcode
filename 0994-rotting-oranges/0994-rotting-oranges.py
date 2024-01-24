class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def get_adjacent_oranges(rotten_oranges):
            """
            rotten oranges를 받고 인접한 셀들의 좌표의 집합을 반환한다.
            (rotten oragnes의 좌표를 제외하고)
            """
            adjacent_oranges = set()
            for i,j in rotten_oranges:
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    x, y = i+dx, j+dy
                    if (
                        x in range(len(grid)) and y in range(len(grid[0]))
                        and grid[x][y] == 1
                    ):
                        adjacent_oranges |= {(x,y)}
            return adjacent_oranges

        rotten_oranges = {
            (i,j)
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j] == 2
        }
        
        fresh_oranges = {
            (i,j)
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if grid[i][j] == 1
        }
        batch_count = 0
        
        """
        1. fresh rotten
        2. fresh not rotten
        3. not fresh rotten
        4. not fresh not rotten
        """
        while fresh_oranges:
            batch_count += 1
            rotting_oranges = fresh_oranges & get_adjacent_oranges(rotten_oranges)
            rotten_oranges |= rotting_oranges
            fresh_oranges -= rotting_oranges
            if not rotting_oranges:
                return -1
        return batch_count
        
"""
# 1.
batch_count += 1
rotting_oranges = fresh_oranges & get_adjacent_oranges(rotten_oranges)
# 이중에서 fresh_oranges랑 겹치면 이번턴에 썩는 애들
# 겹치지 않는 애들은 빈 셀
fresh_oranges -= rotting_oranges
if not rotting_oranges:
    return -1
if not fresh_oranges:
    return batch_count
# 겹치는 fresh 오렌지들을 썩은 오렌지에 추가
# fresh orange에서 제외

# not fresh orange 배치 카운트 반환
# 겹치는게 없으면 -1 반환
"""


    
        
        