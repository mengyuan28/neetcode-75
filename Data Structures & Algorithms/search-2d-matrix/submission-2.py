import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        row_single = [matrix[i][0] for i in range(n)]
        
        row_idx = bisect.bisect_left(row_single, target)
        if row_idx < n and matrix[row_idx][0] == target:
            return True
        
        row_idx -= 1
        if row_idx < 0:
            return False

        all_colmn = [matrix[row_idx][j] for j in range(m)]
        col_idx = bisect.bisect_left(all_colmn, target)
        if col_idx == m:
            return False
        
        return matrix[row_idx][col_idx] == target
