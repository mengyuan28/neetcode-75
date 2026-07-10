from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        ret = [] # tuple (count, item)
        freq_mapping = Counter(nums)
        for item, count in freq_mapping.items():
            if not ret or len(ret) < k: 
                heapq.heappush(ret, (count, item))
            else:
                if ret[0][0] < count:
                    heapq.heappush(ret, (count, item))
                    heapq.heappop(ret)
        result = [t[1] for t in ret]
        result = sorted(result)
        return result