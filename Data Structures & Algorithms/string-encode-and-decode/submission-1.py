class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            cur_len = len(word)
            ret += str(cur_len) + "#" + word
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#' and j < len(s):
                j += 1
            cur_size = int(s[i:j])
            word = s[j+1:j+1+cur_size]
            ret.append(word)
            i = j+cur_size+1
        return ret
