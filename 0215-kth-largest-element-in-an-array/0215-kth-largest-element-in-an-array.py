from collections import Counter
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for key, value in Counter(nums).items():
            heapq.heappush(heap, (-key, value))
        while 0 < k:
            key, value = heappop(heap)
            k -= value
        return -key