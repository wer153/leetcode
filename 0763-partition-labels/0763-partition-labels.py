from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        start, partition_set, answer = 0, set(), list()
        for index, char in enumerate(s, start=1):
            partition_set.add(char)
            counter[char] -= 1
            if all(counter[element] == 0 for element in partition_set):
                answer.append(index-start)
                partition_set.clear()
                start = index
        return answer
