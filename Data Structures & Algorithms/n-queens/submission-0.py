class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        board = [["."] * n for i in range(n)]

        def isSafe(cur_row:int, cur_col:int):
            r = cur_row-1
            while r >= 0:
                if board[r][cur_col] == "Q":
                    return False
                r -= 1
            
            r = cur_row-1
            c = cur_col-1
            while r >= 0 and c >=0:
                if board[r][c] == "Q":
                    return False
                r -=1
                c -=1

            r = cur_row-1
            c = cur_col+1
            while r>=0 and c<n:
                if board[r][c] == "Q":
                    return False
                r -=1
                c +=1
            return True

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ret.append(copy)
            for c in range(0, n):
                if not isSafe(r, c):
                    continue
                board[r][c] = "Q"
                backtrack(r+1)
                board[r][c] = "."
        
        backtrack(0)
        return ret   
        
