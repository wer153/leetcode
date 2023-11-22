class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=True)
        answers = [sorted_intervals[0]]
        for s, e in sorted_intervals[1:]:
            if answers[-1][0] >= e: 
                answers.append([s, e])
            else: 
                count += 1
        return count
