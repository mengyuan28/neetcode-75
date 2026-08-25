class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        n = len(temperatures)
        res = [0] * n
        stack = [] # (temp, index)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                (last_temp, last_index) = stack.pop()
                res[last_index] = i - last_index
            stack.append((t, i))
        return res