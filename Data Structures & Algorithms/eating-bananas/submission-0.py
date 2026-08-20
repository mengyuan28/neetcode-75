from math import ceil
class Solution:
    def canEat(self, piles: List[int], k: int, h: int) -> bool:
        total = 0
        for pile in piles:
            cur_hour = ceil(pile / k)
            total += cur_hour
        return total <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k bananas/hour 
        if not piles:
            return 0
        left = 1
        right = max(piles)
        while left + 1 < right:
            mid = left + (right - left) //2
            if self.canEat(piles, mid, h):
                right = mid
            else:
                left = mid
        if self.canEat(piles, left, h):
            return left
        elif self.canEat(piles, right, h):
            return right
        return -1
        