from collections import Counter

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        for key, value in sorted(Counter(nums).items(), key=lambda x: -x[0]):
            count += value
            if k <= count:
                return key
        