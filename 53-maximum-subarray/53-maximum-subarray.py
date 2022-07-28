class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        largestSum = nums[0]
        tempSum = 0
        
        for element in nums:
            if tempSum < 0:
                tempSum = 0
            tempSum += element
            largestSum = max(largestSum, tempSum) 
        return largestSum 
    # Passing an array of ints called nums
    # return the largest sum from a contiguous subarray
    
    # element: -2
    # tempSum: 0
    # largestSum: 0
    
    
    