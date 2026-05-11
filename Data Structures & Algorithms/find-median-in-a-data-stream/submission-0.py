class MedianFinder:

    def __init__(self):
        self.minh, self.maxh = [], []
        # maxh[0] gives largest
        # minh[0] gives smallest
        # [maxh], [minh]

    def addNum(self, num: int) -> None:
        if self.minh and num > self.minh[0]:
            heapq.heappush(self.minh, num)
        else:
            heapq.heappush(self.maxh, -1* num)
        if len(self.maxh) > len(self.minh) + 1:
            val = -1 * heapq.heappop(self.maxh)
            heapq.heappush(self.minh, val)
        if len(self.minh) > len(self.maxh) + 1:
            val = heapq.heappop(self.minh)
            heapq.heappush(self.maxh, -1* val)

    def findMedian(self) -> float:
        if len(self.maxh) > len(self.minh):
            return -1* self.maxh[0]
        elif len(self.minh) > len(self.maxh):
            return self.minh[0]
        return (-1* self.maxh[0] + self.minh[0]) / 2.0
        
        