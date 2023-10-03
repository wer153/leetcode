from itertools import pairwise

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for index in iterate_peak_index(nums):
            return index


def iterate_peak_index(nums):
    prev = None
    for index, num in enumerate(nums):
        next_ = nums[index+1] if index < len(nums)-1 else None
        if (
            (prev is None or prev < num)
            and (next_ is None or num > next_)
        ):
            yield index 
        prev = num


            
