class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        stack = [c for c in s if c in vowels]
        vowel_reversed = []
        for c in s:
            if c in vowels:
                vowel_reversed.append(stack.pop())
            else:
                vowel_reversed.append(c)
        return ''.join(vowel_reversed)
            