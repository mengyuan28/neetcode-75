class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            cur_len = len(queue)
            for _ in range(cur_len):
                r, c, dis = queue.popleft()
                for dr, dc in direction:
                    nr = r+dr
                    nc = c+dc
                    if 0 <= nr < m and 0 <= nc <n:
                        if dis+1 < grid[nr][nc]:
                            grid[nr][nc] = dis+1
                            queue.append((nr, nc, dis+1))
        return 

