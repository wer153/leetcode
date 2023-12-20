from functools import reduce
from itertools import product


DIGIT_TO_CHARS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def get_next_combinations(combinations, digit):
    return [
        combination + char
        for combination in combinations or ['']
        for char in DIGIT_TO_CHARS[digit]
    ]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        for digit in digits:
            result = get_next_combinations(result, digit)
        return result
        # return list(reduce(get_next_combinations, digits, []))
            