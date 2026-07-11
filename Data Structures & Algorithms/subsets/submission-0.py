class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        my_len = len(nums)
        if my_len == 0:
            return []
        ret = []
        cur_set = []

        def findallCombo(idx:int, cur_set:List[int]):
            ret.append(cur_set[:])
            if idx == my_len:
                # print(cur_set)
                return

            for i in range(idx, my_len, 1):
                cur_set.append(nums[i])
                findallCombo(i+1, cur_set)
                cur_set.pop()

        findallCombo(0, cur_set)
        return ret
