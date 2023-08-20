from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque([])

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q:
            if self.q[-1] - self.q[0] > 3000:
                self.q.popleft()
            else:
                break
            
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)