from functools import cache

class Solution:
    modulo = int(1e9 + 7)
    @cache
    def numTilings(self, n: int) -> int:
        if n==1: return 1
        if n==2: return 2
        if n==3: return 5
        return (
            self.numTilings(n-1)
            + self.numTilings(n-1)
            + self.numTilings(n-3)
        ) % self.modulo