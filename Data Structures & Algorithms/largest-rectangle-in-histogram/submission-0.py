class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # idx, height
        ret = 0
        heights.append(0)
        for idx, height in enumerate(heights):
            start = idx
            # 5, 7, 6
            while stack and stack[-1][1] > height:
                last_idx, last_h = stack.pop(-1)
                area = last_h* (idx - last_idx)
                ret = max(ret, area)
                start = last_idx
            stack.append((start, height))
        return ret
