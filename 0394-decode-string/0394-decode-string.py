from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if c == ']':
                stack += pop_encoded_string(stack) * pop_digit(stack)
        return ''.join(stack)

def pop_encoded_string(stack: list) -> list:
    stack.pop()
    encoded_string = deque([])
    while stack and stack[-1] != '[':
        encoded_string.appendleft(stack.pop())
    stack.pop()
    return encoded_string


def pop_digit(stack: list) -> int:
    count_queue = deque([])
    while stack and stack[-1].isdigit():
        count_queue.appendleft(stack.pop())
    return int(''.join(count_queue))
