import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        my_heap = []
        for stone in stones:
            heapq.heappush(my_heap, -stone)
        
        while len(my_heap) > 1:
            max_first = heapq.heappop(my_heap)
            max_second = heapq.heappop(my_heap)

            diff = max_second - max_first
            if diff > 0:
                heapq.heappush(my_heap, -diff)
        if len(my_heap) == 1:
            return -my_heap[0]
        else:
            return 0
