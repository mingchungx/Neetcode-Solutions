from functools import reduce, xor

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # reduce() is the same as foldr in Racket where we fold it
        return reduce(xor, nums)