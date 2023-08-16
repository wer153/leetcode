from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count, counter = 0, Counter(nums)
        for key, value in counter.items():
            if key == k - key:
                count += counter[key] // 2
            else:
                count += min(counter[key], counter.get(k-key, 0))
            counter[key] = 0
        return count
