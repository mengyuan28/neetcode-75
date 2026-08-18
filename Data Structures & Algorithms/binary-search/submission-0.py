class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        left, right = 0, n-1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

        