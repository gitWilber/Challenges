class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Passing arr of ints called nums: nums[]
        # Passing int called target: int target
        # return list of indices of two numbers that add up to target
        # (nums[], target)
        # return list[i,i]
        
        # Use hashmap to store visted numbers
        # if the difference of target - number is in hashmap, return indices
        
        visited = {}
        
        # for i in range of lenth of array
        for i in range(len(nums)):
            # subtract
            diff = target - nums[i]
            
            # if difference in hashmap
            if diff in visited:
                # return indices
                return [visited[diff], i]
            # else place in hashmap
            # number : index
            else:
                visited[nums[i]] = i
    