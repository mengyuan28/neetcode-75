class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        my_len = len(candidates)
        candidates.sort()

        ret = []
        cur_list = []
        # 1, 2, 2, 4, 5, 6, 9
        def findallCombos(idx: int, cur_sum: int, cur_list:List[int]):
            if cur_sum == target:
                ret.append(cur_list[:])
                return 
            if cur_sum > target:
                return
            if idx == my_len:
                return
            
            i = idx
            while i < my_len:
                if cur_sum + candidates[i] > target:
                    return 
                if i > idx and candidates[i] == candidates[i-1]:
                    i += 1
                    continue
                cur_list.append(candidates[i])
                findallCombos(i+1, cur_sum + candidates[i], cur_list)
                cur_list.pop()
                i += 1

        findallCombos(0, 0, cur_list)

        return ret

                