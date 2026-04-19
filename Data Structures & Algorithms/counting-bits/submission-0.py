class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = []
        for num in range(0, n+1):
            cur_count = 0
            for shift in range(0, 32):
                if (1 << shift) & num:
                    cur_count += 1
            res.append(cur_count)
            # 011 100
        return res

