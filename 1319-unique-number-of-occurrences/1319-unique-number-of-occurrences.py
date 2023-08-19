from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurencies = Counter(arr).values()
        return len(occurencies) == len(set(occurencies))