class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        visitedValues = set()
        
        for n in nums:
            if n in visitedValues:
                return True
            else:
                visitedValues.add(n)
        return False
        
        
        # Use hashset to place visited values
        # if value is in hashmap, then return true
        # else return false
        
        
        
        
        
        # passing nums[int]
        # return true is any value appears at least twice
        # return false if every element is distinct