class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i: int, j:int) -> int:
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        ret = 0
        for i in range(m):
            for j in range(n):
                area = dfs(i, j)
                ret = max(ret, area)
        return ret