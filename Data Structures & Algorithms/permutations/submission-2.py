class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        my_len = len(nums)
        if my_len == 0:
            return []
        ret = []
        cur_list = []
        def findallCombo(cur_list: List[int]):
            if len(cur_list) == my_len:
                ret.append(cur_list[:])
                return
            
            for i in range(0, my_len, 1):
                if nums[i] not in cur_list:
                    cur_list.append(nums[i])
                    findallCombo(cur_list)
                    cur_list.pop()

        findallCombo(cur_list)
        return ret