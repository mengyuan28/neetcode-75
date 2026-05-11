class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m_len = len(nums)
        if m_len == 0:
            return -1
        left, right = 0, m_len-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[mid]:
                if nums[left]<= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
