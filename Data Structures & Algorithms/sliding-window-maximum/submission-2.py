class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return [max(nums)]
        window = [-x for x in nums[0:k]]
        heapq.heapify(window)
        counter = Counter(nums[0:k])
        ret = [-window[0]]
        for i in range(k, len(nums)):
            num = nums[i]
            heapq.heappush(window, -num)
            counter[num] += 1
            old_num = nums[i-k]
            counter[old_num] -= 1
            while window and counter[-window[0]] == 0:
                heapq.heappop(window)
            ret.append(-window[0])
        return ret
