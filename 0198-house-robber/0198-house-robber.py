from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def get_max(index):
            nonlocal nums
            if index == 0: return nums[0]
            if index == 1: return max(nums[0], nums[1])
            return max(
                nums[index] + get_max(index-2),
                get_max(index-1)
            )
        return get_max(len(nums)-1)
