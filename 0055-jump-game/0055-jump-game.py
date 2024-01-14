class Solution:
    def canJump(self, nums: list[int]) -> bool:
        def jump_back(start):
            for index, curr in enumerate(range(start-1, -1, -1), start=1):
                if index <= nums[curr]:
                    return start - index
            return -1

        index = len(nums)-1
        while index != 0:
            index = jump_back(index)
            if index < 0: return False
        return True
