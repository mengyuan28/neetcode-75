from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_num = Counter(tasks) 
        start_time = 0
        q = deque() #(remaining_count_after_running, next_available_time, task_id)
        max_heap = []
        for task_id, count in count_num.items():
            heapq.heappush(max_heap, (-count, task_id))

        #print(max_heap)
        while q or max_heap:
            start_time += 1
            #print(q)
            if not max_heap:
                start_time = q[0][1]
            else:
                count, task_id = heapq.heappop(max_heap)
                remain = -count - 1
                if remain > 0:
                    q.append((remain, start_time+n, task_id))
            if q and q[0][1] == start_time:
                reamin, time, match_id = q.popleft()
                heapq.heappush(max_heap, (-reamin, match_id))
        
        return start_time



