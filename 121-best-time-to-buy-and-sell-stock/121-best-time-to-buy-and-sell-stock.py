class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        maxProfit = 0
        
        while right < len(prices):
            tempProfit = prices[right] - prices[left]
            
            if tempProfit >= 0:
                  maxProfit = max(maxProfit, tempProfit)
            else: 
                left = right
            right += 1
        
        return maxProfit