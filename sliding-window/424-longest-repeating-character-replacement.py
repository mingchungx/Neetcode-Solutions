class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def maxFrequency(substring: str) -> int:
            counter = {i: substring.count(i) for i in set(substring)}
            return max(counter.values())

        left = 0
        maxLength = 0

        for right in range(len(s)):
            substring = s[left: right + 1]
            lenSubstring = right - left + 1
            replacements = lenSubstring - maxFrequency(substring)
            if replacements <= k: # This must be true to have a valid number of replacements
                # Remember the goal is to make a substring be the same character
                maxLength = max(maxLength, lenSubstring)
            else:
                left += 1
        
        return maxLength
