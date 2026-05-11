class Solution:
    def findMin(self, nums: List[int]) -> int:
        m_len = len(nums)
        if m_len == 0:
            return 0
        left, right = 0, m_len-1
        ret = nums[0]
        if nums[left] < nums[right]:
            return nums[left] 
        while left + 1 < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])

                
            