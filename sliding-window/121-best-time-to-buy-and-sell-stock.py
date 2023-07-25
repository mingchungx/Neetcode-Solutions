class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        left, right = 0, 1
        maxProfit = 0
        while (left <= right < len(prices)):
            profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                maxProfit = max(profit, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit