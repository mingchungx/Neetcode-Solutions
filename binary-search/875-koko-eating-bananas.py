from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        k = right # we know all will be less or equal to max(piles)
        while (left <= right):
            mid = (left + right) // 2 # k value
            time = 0
            for bananas in piles:
                time += ceil(bananas / mid)
            if time <= h:
                k = min(k, mid)
                right = mid - 1
            else:
                left = mid + 1

        return k