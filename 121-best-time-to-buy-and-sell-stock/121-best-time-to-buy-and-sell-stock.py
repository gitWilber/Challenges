class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # can use 2 pointers to subtract
        buy, sell = 0, 1
        maxProfit = 0
        
        # while second pointer in range of list
        for sell in range(len(prices)):
            # temp profit is price of day sold - day bought
            tempProfit = prices[sell] - prices[buy]
            # if temp profit is not negative
            if tempProfit > 0:
                # compare profits to see which is max
                maxProfit = max(maxProfit, tempProfit)
            # else we move the first pointer
            else:
                buy = sell
            # increment second pointer
            sell += 1
        # return max profit after comparing all days
        return maxProfit
            
        
        
        
        
        # passing array prices
        # return the maxProfit
        # i represent day