from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        local_sum = 0
        for index, num in enumerate(nums):
            if local_sum + num == total_sum - local_sum:
                return index
            local_sum += num
        return -1
