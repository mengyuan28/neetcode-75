class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        m_len = len(intervals)
        if m_len == 0:
            return 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        prevEnd = intervals[0][1]
        ret = 0
        for i in range(1, m_len):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                ret += 1
                prevEnd = min(intervals[i][1], prevEnd)
        return ret
