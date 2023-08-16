from collections import deque

class Solution:
    def compress(self, chars: List[str]) -> int:
        result: list[str] = []
        count: int = 0
        old_c: str = ''
        for c in chars:
            if c != old_c:
                if count > 1:
                    result.extend(list(str(count)))
                count = 1
                old_c = c
                result.append(c)
            else:
                count += 1
        if count > 1:
            result.extend(list(str(count)))
        chars[:] = result[:]
        return len(chars)
