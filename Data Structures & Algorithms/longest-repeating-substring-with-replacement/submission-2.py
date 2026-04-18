class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_set = set(s)
        for c in char_set:
            count, left = 0, 0
            for right in range(0, len(s)):
                if s[right] == c:
                    count += 1
                
                # means couldn't fill within k to match
                while (right - left + 1) - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1

                res = max(res, right - left + 1)

        return res
