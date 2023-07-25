class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits) - 1 # Keep track of cur, starts at end

        def add(digits, n):
            if n < 0:
                return
            if n == 0 and digits[n] == 9:
                digits[n] = 0
                digits.insert(0, 1)
            elif digits[n] == 9:
                digits[n] = 0
                add(digits, n - 1)
            else:
                digits[n] = digits[n] + 1

        add(digits, n)

        return digits