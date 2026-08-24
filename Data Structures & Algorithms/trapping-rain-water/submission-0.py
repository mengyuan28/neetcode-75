class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        max_left_height = 0
        max_right_height = 0
        ret = 0
        while left < right:
            if height[left] < height[right]:
                max_left_height = max(max_left_height, height[left])
                ret += max_left_height - height[left]
                left += 1
            else:
                max_right_height = max(max_right_height, height[right])
                ret += max_right_height - height[right]
                right -= 1
        return ret


