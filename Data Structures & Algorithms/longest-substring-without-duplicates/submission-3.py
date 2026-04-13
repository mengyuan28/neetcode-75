class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_len = len(s)
        i = 0
        max_len = 0
        cur_win = set()
        left = 0
        for i in range(0,cur_len):
            while s[i] in cur_win:
                cur_win.remove(s[left])
                left += 1

            cur_win.add(s[i])
            max_len = max(max_len, i-left + 1)
        return max_len
