class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Time Complexity: Sort = O(logn) + Two nested for loops = O(n^2) = O(logn) + O(n^2) = O(n^2)
        
        # Sort nums array
        nums.sort()
        result = []
        
        # i = index, value = actual number
        for i, value in enumerate(nums):
            # if index is greater than zero and value is same as previous value
            # we end current iteration, go straight to next value
            if i > 0 and value == nums[i - 1]:
                    continue
            
            # Use left and right pointer to add
            left, right = i + 1, len(nums) - 1
            # while left pointer remains before right, we calculate
            while left < right:
                theSum = value + nums[left] + nums[right]
                # if sum is negative, move left pointer right
                if theSum < 0:
                    left +=1
                # if sum is greater than 0, move right pointer left
                elif theSum > 0:
                    right -= 1
                # else sum is 0, put all 3 numbers in result
                else:
                    result.append([value, nums[left], nums[right]])
                    # Move left pointer forward
                    left += 1
                    # incase left pointer is equal to previous value, keep moving left pointer
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        
        return result