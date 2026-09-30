class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        if fresh == 0:
            return 0
        step = 0
        while queue:
            cur_len = len(queue)
            for _ in range(cur_len):
                r, c = queue.popleft()
                for dr, dc in direction:
                    nr = r+dr
                    nc = c+dc
                    if 0 <= nr < m and 0<= nc < n:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
                            fresh -= 1
            step +=1
        if fresh == 0:
            return step-1
        return -1
                