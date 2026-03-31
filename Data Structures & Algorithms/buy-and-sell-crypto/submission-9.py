class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        seen = []
        maxProfit = 0

        p1=0
        p2=1

        while p2 < len(prices):
            maxProfit = max(maxProfit, prices[p2] - prices[p1])
            if prices[p1] > prices[p2]:
                p1 = p2
                p2 += 1
            else:
                p2 += 1
            

        return maxProfit


         
