from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        my_len = len(s)
        if my_len == 0:
            return []
        ret = []
        cur_list = []

        def validPalindrom(s: str) -> bool:
            left = 0
            right = len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def findAllCombos(index: int, cur_list:List[str]):
            if index == my_len:
                ret.append(cur_list[:])
                return
            
            for i in range(index, my_len):
                substring = s[index:i+1]
                if validPalindrom(substring):
                    cur_list.append(substring)
                    findAllCombos(i+1, cur_list)
                    cur_list.pop()

        findAllCombos(0, cur_list)
        return ret
                