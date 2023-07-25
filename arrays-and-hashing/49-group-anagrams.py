class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # We map each of the strings to be its sorted version and group those with the same map
        hm = dict()

        # O(n)
        for word in strs:
            sort = "".join(sorted(word))
            # Make it an array
            if sort not in hm:
                hm[sort] = []
            hm[sort].append(word)

        return hm.values()