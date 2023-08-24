class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        temp = (a|b)^c
        return list(f'{temp&a:b}{temp&b:b}{temp&c:b}').count('1')