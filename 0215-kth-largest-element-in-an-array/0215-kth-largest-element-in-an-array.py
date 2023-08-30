from heapq import heapify, nlargest, nsmallest
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k < len(nums)//2:
            return nlargest(k, nums)[-1]
        return nsmallest(len(nums)-k+1, nums)[-1]
