from heapq import heapify, heappop, heappush
class SmallestInfiniteSet:

    def __init__(self):
        self.start = 1
        self._pq = []
        self._pq_set = set()

    def popSmallest(self) -> int:
        if self._pq:
            value = self._heappop()
            if self.start <= value:
                if self.start < value:
                    self._heappush(value)
                value = self.start
                self.start += 1
        else:
            value = self.start
            self.start += 1
        return value

    def addBack(self, num: int) -> None:
        if num < self.start:
            self._heappush(num)

    def _heappop(self):
        value = heappop(self._pq)
        self._pq_set.remove(value)
        return value

    def _heappush(self, value):
        if value not in self._pq_set:
            heappush(self._pq, value)
            self._pq_set.add(value)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)