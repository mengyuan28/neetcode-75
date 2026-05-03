class Solution:
    def longestPalindrome(self, s: str) -> str:
        m_len = len(s)
        if m_len == 0:
            return ""
        max_len = 0
        max_index = 0
        for i in range(m_len):
            l, r = i, i
            while l >=0 and r < m_len and s[l] == s[r]:
                cur_len = r-l+1
                if cur_len > max_len:
                    max_len = cur_len
                    max_index = l
                l -= 1
                r += 1
            l, r = i, i+1
            while l >=0 and r < m_len and s[l] == s[r]:
                cur_len = r-l+1
                if cur_len > max_len:
                    max_len = cur_len
                    max_index = l
                l -= 1
                r += 1
        return s[max_index: max_index+max_len]
