class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if stack[-1] == '*':
                stack.pop()
                stack.pop()
        return ''.join(stack)