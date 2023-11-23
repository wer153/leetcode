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
        def generate_chars(chars, max_length=len(digits)):
            if len(chars) == max_length:
                answer.append(chars)
                return
            for char in digit_to_chars[digits[len(chars)]]:
                generate_chars(chars+char)
        answer = []
        generate_chars('')
        return [word for word in answer if word]
    
        
            
            
            