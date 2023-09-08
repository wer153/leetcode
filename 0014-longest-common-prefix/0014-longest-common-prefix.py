class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        for chars in zip(*strs):
            if set(chars) == {chars[0]}:
                answer.append(chars[0])
            else:
                break
        return ''.join(answer)
