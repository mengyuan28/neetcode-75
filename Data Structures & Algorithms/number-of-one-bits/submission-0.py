class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        print(n)
        while n > 0:
            res += n%2
            print(res)
            n = n // 2
        return res