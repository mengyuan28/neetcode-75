from dataclasses import dataclass
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]) -> int:
            return (point[0])**2 + (point[1])**2
        
        max_heap = []
        ret = []
        for point in points:
            cur_dis = distance(point)
            print(f"{cur_dis} for point: {point}")
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-cur_dis, point))

            elif cur_dis < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-cur_dis, point))
        
        while max_heap:
            dis, cur_point = heapq.heappop(max_heap)
            ret.append(cur_point)
        return ret


