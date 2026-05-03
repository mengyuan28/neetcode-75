class Solution:
    def numDecodings(self, s: str) -> int:
        m_len = len(s)
        if m_len == 0:
            return 1
        dp = [0] * (m_len+1)
        dp[0] = 1
        for i in range(0, m_len):
            if s[i] != "0":
                dp[i+1] += dp[i]
            if i > 0 and (s[i-1] == "1" or (s[i-1] == "2" and s[i] in "0123456")):
                dp[i+1] += dp[i-1]
        return dp[m_len]