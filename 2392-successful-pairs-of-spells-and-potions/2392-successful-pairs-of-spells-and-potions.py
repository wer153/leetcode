from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def get_num_of_pair(spell):
            return len(potions) - bisect_left(potions, success / spell)
        potions.sort()
        return [get_num_of_pair(spell) for spell in spells]
