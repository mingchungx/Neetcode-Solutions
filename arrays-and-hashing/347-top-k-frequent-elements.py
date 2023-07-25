import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # O(1) case - nothing to consider
        if k == nums:
            return nums

        # Make a counter map
        hm = {i: nums.count(i) for i in set(nums)}

        # Return the n largest of the keys using a heapq
        return heapq.nlargest(k, hm.keys(), key=hm.get)