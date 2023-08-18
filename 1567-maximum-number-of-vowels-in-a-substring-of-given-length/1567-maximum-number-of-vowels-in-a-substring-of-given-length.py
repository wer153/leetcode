class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_vowels = curr = len([c for c in s[:k] if c in vowels])
        for index, c in enumerate(s[k:], k):
            if c in vowels:
                curr += 1
            if s[index - k] in vowels:
                curr -= 1
            max_vowels = max(max_vowels, curr)
        return max_vowels
