import bisect
class TimeMap:

    def __init__(self):
        self.mapping = defaultdict(list) # key -> list

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        cur_list = self.mapping[key]

        idx = bisect.bisect_right(cur_list, timestamp, key = lambda x: x[1])
        if idx == len(cur_list):
            return cur_list[-1][0]
        if idx == 0:
            return ""
        return cur_list[idx-1][0]
