class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top k, max heap
        # get count first
        frequency = Counter(nums)
        max_heap = []
        ret = []
        for val, count in frequency.items():
            heapq.heappush(max_heap, (-count, val))
        while k > 0:
            count, val = heapq.heappop(max_heap)
            ret.append(val)
            k -=1 
        return ret