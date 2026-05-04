class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        m_len = len(nums)
        if m_len == 0:
            return 0
        dp = [1] * m_len
        ret = 1
        for i in range(m_len):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
            ret = max(ret, dp[i])
        return ret
        