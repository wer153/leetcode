from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(combination) for combination in combinations(range(1,10), r=k) if sum(combination) == n]