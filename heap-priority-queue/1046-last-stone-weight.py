from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # We will use a min-heap
        # negating values in stones makes biggest the smallest

        stones = [-i for i in stones]
        heapify(stones)

        while (stones):
            heaviest = -heappop(stones)
            if not stones:
                return heaviest
            secondHeaviest = -heappop(stones)
            if heaviest > secondHeaviest:
                heappush(stones, secondHeaviest - heaviest)

        return 0