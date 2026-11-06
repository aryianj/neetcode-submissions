class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit: int = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    mProfit = max(mProfit, prices[j] - prices[i])
        return mProfit