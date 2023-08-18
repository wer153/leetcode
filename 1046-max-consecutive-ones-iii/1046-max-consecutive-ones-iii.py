from collections import deque

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        queue = deque()
        count = 0
        answer = 0
        for num in nums:
            queue.append(num)
            if num == 0:
                count += 1
            while k < count:
                first = queue.popleft()
                if first == 0:
                    count -= 1
            answer = max(answer, len(queue))
        return answer
