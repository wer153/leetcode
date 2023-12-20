digit_to_chars = {
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
        def generate_next_combinations(chars):
            for combination in combinations or ['']:
                for char in chars:
                    yield combination + char

        combinations = []
        for digit in digits:
            combinations = [
                combination for combination
                in generate_next_combinations(digit_to_chars[digit])
            ]
        return combinations
    
            
            
            