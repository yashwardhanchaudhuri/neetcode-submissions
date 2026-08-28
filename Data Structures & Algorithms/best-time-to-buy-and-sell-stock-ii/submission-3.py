class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = []
        for i in range(1, len(prices)):
            result.append(prices[i] - prices[i-1])
        sum = 0
        for i in result:
            if i > 0:
                sum += i
        return sum
        