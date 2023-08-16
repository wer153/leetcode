class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index, count = 0, 0
        while count < len(s) and index < len(t):
            if t[index] == s[count]:
                count += 1
            index += 1
        return count == len(s)
