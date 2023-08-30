from collections import deque

class RecentCounter:

    def __init__(self):
        self._q = deque([])

    def ping(self, t: int) -> int:
        self._q.append(t)
        while self._q and self._q[-1] - self._q[0] > 3000:
            self._q.popleft()
        return len(self._q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)