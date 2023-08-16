class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_nums_of_candies = max(candies)
        return [
            max_nums_of_candies <= candy + extraCandies
            for candy in candies
        ]