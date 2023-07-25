class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Get a character set
        charSet = set()

        # Use sliding window approach
        left = 0
        maxLength = 0

        for right in range(len(s)):
            # Making sure our substring is non repeating characters
            while (s[right] in charSet):
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
            
        return maxLength