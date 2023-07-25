class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Ignore casing, skip non-alphanumeric characters
        # Alphanumeric characters include only: numbers and letters
        i, j = 0, len(s) - 1

        while (i < j):
            # Deal with casing
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                else:
                    # Shift inward
                    i, j = i + 1, j - 1
                    continue
            # Deal with non-alphanumeric characters
            if not a.isalnum():
                i += 1
            if not b.isalnum():
                j -= 1
            
        return True