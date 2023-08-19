from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word_counter1, word_counter2 = Counter(word1), Counter(word2)
        return (
            set(word_counter1) == set(word_counter2)
            and sorted(word_counter1.values()) == sorted(word_counter2.values())
        )
