class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count, index = 0, 0
        while index < len(nums):
            if nums[index] == 0:
                del nums[index]
                index -= 1
                count += 1
            index += 1
        nums.extend([0] * count)
