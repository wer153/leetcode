class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list({num: None for num in nums}.keys())
        return len(nums)
        