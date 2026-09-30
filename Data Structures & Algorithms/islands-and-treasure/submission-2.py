class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in direction:
                nr = r+dr
                nc = c+dc
                if 0 <= nr < m and 0 <= nc <n:
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr, nc))
        return 

