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


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def get_next_combinations(chars):
            return [
                combination + char
                for combination in combinations or ['']
                for char in chars
            ]

        combinations = []
        for digit in digits:
            combinations = get_next_combinations(DIGIT_TO_CHARS[digit])
        return combinations
            