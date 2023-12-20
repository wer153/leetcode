from collections import deque
from operator import itemgetter

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        points.sort(key=itemgetter(1,0), reverse=True)
        while points:
            start, end = points.pop()
            count += 1
            while points and points[-1][0] <= end:
                points.pop()
        return count