class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m_len = len(nums)
        if m_len == 0:
            return 0
        dp = [0] * m_len
        min_dp = [0] * m_len
        ret = float("-inf")
        for i in range(0, m_len):
            dp[i] = nums[i]
            min_dp[i] = nums[i]
            if i > 0:
                dp[i] = max(dp[i], dp[i-1]*nums[i], min_dp[i-1] * nums[i])
                min_dp[i] = min(min_dp[i], dp[i-1]*nums[i], min_dp[i-1] * nums[i])
            ret = max(ret, dp[i])
        print(dp)
        return ret
