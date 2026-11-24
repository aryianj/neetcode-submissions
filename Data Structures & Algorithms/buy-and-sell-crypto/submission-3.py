class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = float("-inf")
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxP = max(maxP, prices[j] - prices[i])
        return int(maxP)