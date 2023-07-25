class Solution:
    def sumSquaredDigits(self, n: int) -> int:
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum


    def isHappy(self, n: int) -> bool:
        # 3 possibilites: n -> 1, n -> cycles, n -> infinity
        # However n -> infinity doesn't happen because if n is comprised of only 9s, 
        # then n must cycle at, or under the value of 9^2 + 9^2 + ...(n times) + 9^2
        # So we only need to consider if n -> 1 or n -> cycle
        # Let's detect cycle

        found = []

        while n != 1:
            if n in found:
                return False
            found.append(n)
            n = self.sumSquaredDigits(n)

        return True