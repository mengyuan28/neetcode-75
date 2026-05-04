class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m_len = len(s)
        if m_len == 0:
            return False
        dp = [False] * (m_len+1)
        dp[0] = True
        for i in range(0, len(s)):
            for word in wordDict:
                c = len(word)
                if i-c+1 >= 0:
                    if s[i-c+1: i+1] == word:
                        dp[i+1] = dp[i-c+1] or dp[i+1]
        return dp[m_len]