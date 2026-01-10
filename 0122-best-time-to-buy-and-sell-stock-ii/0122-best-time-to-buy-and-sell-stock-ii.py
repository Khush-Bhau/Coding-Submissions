class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        
        # Iterate through the array starting from the second day
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, we 'buy' yesterday and 'sell' today
            # We add this difference to our total profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit