from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def climb(index):
            nonlocal cost
            if index == 0: return cost[0]
            if index == 1: return cost[1]
            return min(climb(index-1), climb(index-2)) + cost[index]
        cost.append(0)
        return climb(len(cost)-1)