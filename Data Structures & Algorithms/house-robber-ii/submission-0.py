class Solution:
    def orob(self, nums:List[int]) -> int:
        m_len = len(nums)
        dp = [0] * m_len
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, m_len):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[m_len-1]

    def rob(self, nums: List[int]) -> int:
        m_len = len(nums)
        if m_len == 1:
            return nums[0]
        if m_len == 2:
            return max(nums[0], nums[1])
        ret1 = self.orob(nums[1:])
        ret2 = self.orob(nums[0:m_len-1])
        return max(ret1, ret2)
