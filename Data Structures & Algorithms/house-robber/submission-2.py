class Solution:
    def rob(self, nums: List[int]) -> int:
        m_len = len(nums)
        if m_len == 0:
            return 0
        if m_len == 1:
            return nums[0]
        if m_len == 2:
            return max(nums[0], nums[1])
        dp = [0] * m_len
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, m_len):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        print(dp)
        return dp[m_len-1]

        