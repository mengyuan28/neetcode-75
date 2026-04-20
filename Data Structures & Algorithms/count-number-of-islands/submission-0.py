class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 
        if grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        if col == 0:
            return 0
        count = 0
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count


