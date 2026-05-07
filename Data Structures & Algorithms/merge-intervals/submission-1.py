class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = []
        for interval in intervals:
            if not ret or interval[0] > ret[-1][1]:
                ret.append(interval)
            else:
                prev_end = ret[-1][1]
                ret[-1][1] = max(interval[1], prev_end)
        return ret