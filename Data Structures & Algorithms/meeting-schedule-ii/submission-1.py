"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_room = 0
        m_len = len(intervals)
        if m_len == 0:
            return 0
        points = []
        for interval in intervals:
            points.append((interval.start, 1))
            points.append((interval.end, -1))
        points.sort(key = lambda x: (x[0], x[1]))
        cur = 0
        for t, c in points:
            cur += c
            max_room = max(max_room, cur)
        return max_room

        
        