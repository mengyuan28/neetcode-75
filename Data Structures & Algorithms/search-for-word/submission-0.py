class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        visited = set()

        def dfs(row: int, col: int, i: int) -> bool:
            if i == len(word):
                return True
            if row < 0 or col < 0 or row >=m or col >=n or board[row][col] != word[i] or (row, col) in visited:
                return False
            visited.add((row, col))
            res = dfs(row+1, col, i+1) or dfs(row, col+1, i+1) or dfs(row-1, col, i+1) or dfs(row, col-1, i+1)
            visited.remove((row, col))
            return res
        for i in range(0, m):
            for j in range(0, n):
                if dfs(i, j, 0):
                    return True
        return False

