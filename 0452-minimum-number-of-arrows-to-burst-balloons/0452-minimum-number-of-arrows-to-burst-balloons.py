from collections import deque
from operator import itemgetter

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        dq = deque(sorted(points, key=itemgetter(1,0)))
        while dq:
            start, end = dq.popleft()
            count += 1
            while dq and dq[0][0] <= end:
                dq.popleft()
        return count