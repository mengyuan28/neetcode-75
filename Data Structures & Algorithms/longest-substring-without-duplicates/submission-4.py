class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_len = len(s)
        if cur_len == 0:
            return 0
        max_len = 0
        left = 0
        check = set()
        for i in range(0, cur_len):
            while s[i] in check:
                check.remove(s[left])
                left += 1
            check.add(s[i])
            sub_len = i - left + 1
            max_len = max(max_len, sub_len)
        return max_len
