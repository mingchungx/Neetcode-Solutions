class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Create a set of found elements
        found = set()

        # If any have appeared, then must be a duplicate
        for i in nums:
            if i in found:
                return True
            found.add(i)

        # Otherwise there are no duplicates
        return False