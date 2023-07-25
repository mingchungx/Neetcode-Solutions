class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 in s2

        def isPermutation(str1: str, str2: str) -> bool:
            # Permutation if all letters are the same and their counts are the same
            return {i: str1.count(i) for i in set(str1)} == {i: str2.count(i) for i in set(str2)}

        left, right = 0, 0
        while (left <= right < len(s2)):
            substringLength = right - left + 1

            # Make the substrings equal in length
            while (substringLength < len(s1)):
                right += 1
                substringLength = right - left + 1
            
            # Using index splicing to get the right window
            if isPermutation(s1, s2[left: right + 1]):
                return True
            else:
                left += 1
        return False