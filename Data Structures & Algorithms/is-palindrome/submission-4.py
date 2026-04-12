class Solution:
    def isAlphaNum(self, s: str) -> bool:
        if ord('A') <= ord(s) <= ord('Z'):
            return True
        elif ord('a') <= ord(s) <= ord('z'):
            return True
        elif ord('0') <= ord(s) <= ord('9'):
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        m_len = len(s)
        if m_len == 0:
            return True
        i, j = 0, m_len-1
        while i < j:
            while i < j and not self.isAlphaNum(s[i]):
                i += 1
            while i < j and not self.isAlphaNum(s[j]):
                j -= 1
            if i < j:
                if s[i].lower()!= s[j].lower():
                    return False
                i += 1
                j -= 1
        return True