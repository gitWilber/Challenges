class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # left and right pointer for difference
        left, right = 0, 1
        # max profit variable
        maxProfit = 0
        
        # while right is in bounds (length of the prices list)
        while right < len(prices):
            # temp profit is difference between two pointers
            tempProfit = prices[right] - prices[left]
            # if there is a profit, we compare to temp and max profit
            if tempProfit >= 0:
                  maxProfit = max(maxProfit, tempProfit)
            # else left pointer will equal to the right one
            else: 
                left = right
            # always increment right pointer
            right += 1
        # return max profit
        return maxProfit