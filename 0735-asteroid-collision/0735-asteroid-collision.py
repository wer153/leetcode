class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = []
        stack = []
        for asteroid in asteroids:
            if 0 < asteroid:
                stack += [asteroid]
            else:
                while stack:
                    if abs(stack[-1]) < abs(asteroid):
                        stack.pop()
                    else:
                        if abs(stack[-1]) == abs(asteroid):
                            stack.pop()
                        break
                else:
                    answer += [asteroid]
        answer += stack 
        return answer
