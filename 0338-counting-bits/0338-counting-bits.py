from functools import cache

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bit_counter(num) for num in range(n+1)]
    
@cache
def bit_counter(num):
    if num == 0: return 0
    return bit_counter(num //2) + num % 2
