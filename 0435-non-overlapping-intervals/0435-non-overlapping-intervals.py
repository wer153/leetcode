class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=True)
        non_overlapped_intervals = [sorted_intervals[0]]
        for start, end in sorted_intervals[1:]:
            if non_overlapped_intervals[-1][0] >= end: 
                non_overlapped_intervals.append([start, end])
            else: 
                count += 1
        return count
