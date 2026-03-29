class Solution:
    def validPair(self, l: str, r: str) -> bool:
        if l == "[" and r == "]":
            return True
        if l == "{" and r == "}":
            return True
        if l == "(" and r == ")":
            return True 
        return False
    def isValid(self, s: str) -> bool:
        stk = []
        if len(s) == 1:
            return False
        for char in s:
            if char in "[({":
                stk.append(char)
            else:
                if not stk:
                    return False
                cur_top = stk[-1]
                if not self.validPair(cur_top, char):
                    return False
                stk.pop()
        print()
        return len(stk) == 0

