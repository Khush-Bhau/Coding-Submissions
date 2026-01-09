class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min_price = float('inf')  # Initialize to a very high value
        max_profit = 0            # Initialize max profit to 0
        
        for price in prices:
            # Update the minimum price seen so far
            if price < min_price:
                min_price = price
            
            # Calculate the profit if we sold at the current price
            # and update max_profit if this profit is higher
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit