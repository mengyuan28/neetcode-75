"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        cur_len = len(intervals)
        if cur_len <= 1:
            return True
        intervals.sort(key=lambda i: i.start)
        for i in range(1, cur_len):
            prev_end = intervals[i-1].end
            if intervals[i].start < prev_end:
                return False
        return True
