from itertools import pairwise
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        indeces = (
            index
            for index, flowerbed in enumerate([1,0] + flowerbed + [0,1])
            if flowerbed == 1
        )
        return n <= sum(
            (distance - 2) // 2
            for distance in [b - a for a, b in pairwise(indeces)]
        )
