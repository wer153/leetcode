from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums) - 1
        while 0 <= j:
            pair = target - nums[j]
            if pair in nums and nums.index(pair) != j:
                return [nums.index(pair), j]
            j -= 1
                
