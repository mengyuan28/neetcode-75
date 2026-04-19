class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur_len = len(nums)
        if cur_len == 0:
            return -1
        nums.sort()
        nums.append(0)
        for i in range(0, cur_len+1):
            print(nums[i])
            if nums[i] != i:
                return i
        return -1
