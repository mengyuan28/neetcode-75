class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_len = len(nums)
        if m_len == 0:
            return 0
        cur_sum = 0
        ret = nums[0]
        for num in nums:
            cur_sum += num
            ret = max(ret, cur_sum)
            if cur_sum < 0:
                cur_sum = 0

        return ret