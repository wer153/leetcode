class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = curr_sum = sum(nums[:k])
        for index, num in enumerate(nums[k:], k):
            curr_sum = curr_sum - nums[index-k] + num
            max_sum = max(max_sum, curr_sum)
        return max_sum / k
