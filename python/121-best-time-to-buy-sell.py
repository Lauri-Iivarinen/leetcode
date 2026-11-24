def maxProfit(self, prices):
        pot = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] - prices[l] > pot:
                pot = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        return pot
