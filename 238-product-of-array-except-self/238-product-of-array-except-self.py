class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # array is equal to the product of all elements of nums except for nums[i]
        # answer = [1, 1, 1, 1]
        answer = [1] * len(nums)
        
        # prefix starts at 1 so we can multiply
        # answer = [1, 1, 2, 6]
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        # postix is 1 so we can multiply last value in answer array
        # answer = [24, 12, 8, 6]
        postfix = 1
        for i in range(len(nums) -1 , -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer