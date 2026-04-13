class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        cur_len = len(nums)
        ret = []
        for i in range(cur_len-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, cur_len-1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        return ret
