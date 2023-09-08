class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        half = len(s)//2
        return all(
            a == b for a,b in zip(s[:half], s[::-1][:half])
        )
        