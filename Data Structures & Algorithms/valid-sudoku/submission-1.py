class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        if rows != 9:
            return False
        cols = len(board[0])
        if cols != 9:
            return False

        def checkrows() -> bool:
            for i in range(0, rows):
                check = set()
                for j in range(0, cols):
                    if board[i][j] != ".":
                        if board[i][j] in check:
                            return False
                        check.add(board[i][j])
            return True
        
        def checkcols() -> bool:
            for j in range(0, cols):
                check = set()
                for i in range(0, rows):
                    if board[i][j] != ".":
                        if board[i][j] in check:
                            return False
                        check.add(board[i][j])
            return True

        def checksub(rowoffs: int = 0, coloffs: int = 0) -> bool:
            check = set()
            for i in range(rowoffs, rowoffs+3, 1):
                for j in range(coloffs, coloffs+3, 1):
                    if board[i][j] != ".":
                        if board[i][j] in check:
                            return False
                        check.add(board[i][j])
            return True

        if not checkrows():
            return False
        if not checkcols():
            return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not checksub(i, j):
                    return False
        return True
                    
                    


                


        