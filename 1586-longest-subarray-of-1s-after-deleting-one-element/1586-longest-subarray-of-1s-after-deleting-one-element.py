from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        answer = 0
        queue = deque()
        for num in nums:
            queue.append(num)
            if num == 0:
                count += 1
            while 1 < count:
                first = queue.popleft()
                if first == 0:
                    count -= 1
            answer = max(answer, len(queue))
        if count == len(nums):
            return 0
        return answer - 1
