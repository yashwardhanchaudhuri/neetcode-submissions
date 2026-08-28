class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i-1]
            sum += temp if temp > 0 else 0
        return sum
        