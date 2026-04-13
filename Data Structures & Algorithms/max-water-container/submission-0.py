class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        cur_len = len(heights)
        i, j = 0, cur_len-1
        while i < j:
            if heights[i] < heights[j]:
                cur_area = heights[i] * (j-i)
                max_area = max(max_area, cur_area)
                i += 1
            else:
                cur_area = heights[j] * (j-i)
                max_area = max(max_area, cur_area)
                j -= 1
        return max_area

