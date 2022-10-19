class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Make answer length of nums
        # prefix and postfix are both equal to 1
        answer = [1] * len(nums)
        prefix, postfix = 1, 1
        
        # First iteration multiplies by prefix
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Last iteration starts at the end and multiplies by postfix until the start
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
            
        return answer
    # Answer = [24, 12, 8, 6]