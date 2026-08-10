class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map:Dict[str, str] = {"2":"abc", "3":"def","4":"ghi", "5":"jkl", 
        "6":"mno","7":"pqrs","8":"tuv", "9":"wxyz"}
        ret = []
        def dfs(pos: int, cur_path: List[str], sub_index:int):
            if pos == len(digits):
                ret.append("".join(cur_path))
                return
            
            cur_digit = digits[pos]
            if cur_digit not in digit_map:
                return 
                
            for j in range(0, len(digit_map[cur_digit])):
                cur_path.append(digit_map[cur_digit][j])
                dfs(pos+1, cur_path, j)
                cur_path.pop(-1)

        cur_path = []
        dfs(0, cur_path, 0)
        return ret;