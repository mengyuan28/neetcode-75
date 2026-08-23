import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap: List[int] = []
        self.k = k
        cur_count = 0
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
                print(self.heap)
            else:
                if len(self.heap) >= k and self.heap[0]<num:
                    it = heapq.heappop(self.heap)
                    print(f"popping out: {it}")
                    heapq.heappush(self.heap, num)
                    print(f"adding: {num}")
            
        print(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0]<val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]

    #  4, 5, 8
        
