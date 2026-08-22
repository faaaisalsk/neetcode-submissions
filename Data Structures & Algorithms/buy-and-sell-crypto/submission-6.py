class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        res = 0
        l = 0
        r = 1
        n = len(prices)
        while r < n:
            if prices[l]> prices[r]:
                l = r
            elif prices[l]< prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            r +=1
        return res
