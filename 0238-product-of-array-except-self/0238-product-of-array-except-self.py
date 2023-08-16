from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 1 < nums.count(0):
            return [0] * len(nums)
        product = reduce(mul, (num for num in nums if num != 0))
        if 1 == nums.count(0):
            return [
                product if num == 0 else 0
                for num in nums
            ]
        return [product // num for num in nums]
