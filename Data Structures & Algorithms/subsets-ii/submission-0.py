class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        my_len = len(nums)

        curlist = []
        ret = []
        nums.sort()

        def findSubs(idx: int, curlist: List[int]):
            ret.append(curlist[:])
            
            if idx == my_len:
                return 

            i = idx
            while i < my_len:
                if i > idx and nums[i] == nums[i-1]:
                    i += 1
                    continue
                curlist.append(nums[i])
                findSubs(i+1, curlist)
                curlist.pop()
                i += 1
        findSubs(0, curlist)
        return ret