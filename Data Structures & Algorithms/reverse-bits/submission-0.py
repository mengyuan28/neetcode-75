class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n & (1 << i):
                binary += "1"
            else:
                binary += "0"
        res = 0
        for i, bit in enumerate(binary[::-1]):
            if bit == "1":
                res += pow(2, i)
        return res