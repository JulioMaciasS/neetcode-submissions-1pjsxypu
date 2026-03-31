class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = []
        maxProfit = 0

        for i,oldPrice in enumerate(prices):
            if oldPrice not in seen:
                seen.append(oldPrice)
                currentMax=0
                for newPriceIndex in range(i, len(prices)):
                    currentMax = max(currentMax, prices[newPriceIndex] - oldPrice)
                maxProfit = max(currentMax, maxProfit)

        return maxProfit


         
