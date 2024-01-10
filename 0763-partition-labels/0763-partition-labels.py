from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        return [len(partition) for partition in generate_partitions(s)]

def generate_partitions(string):
    counter = Counter(string)
    start, partition_set = 0, set()
    for index, char in enumerate(string, start=1):
        partition_set.add(char)
        counter[char] -= 1
        if all(counter[element] == 0 for element in partition_set):
            yield string[start:index]
            partition_set.clear()
            start = index
