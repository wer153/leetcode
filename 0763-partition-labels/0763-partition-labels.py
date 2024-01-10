from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        return [len(partition) for partition in generate_partitions(s)]

def generate_partitions(string):
    counter = Counter(string)
    partition_list, partition_set = list(), set()
    for char in string:
        partition_list.append(char)
        partition_set.add(char)
        counter[char] -= 1
        if all(counter[element] == 0 for element in partition_set):
            yield partition_list
            partition_list, partition_set = list(), set()

        
    