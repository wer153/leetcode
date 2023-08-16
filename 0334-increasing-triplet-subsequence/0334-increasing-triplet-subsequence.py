from sys import maxsize

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left, mid = maxsize, maxsize
        for num in nums:
            if mid < num:
                return True
            if left < num < mid:
                mid = num
            elif num < left:
                left = num
        else:
            return False
                
