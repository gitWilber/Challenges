class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Use a set to place visited numbers
        visitedValues = set()
        # for number in the list
        for n in nums:
            # if the number is in the set, there are duplicates
            if n in visitedValues:
                return True
            # else we add the number into the set
            else:
                visitedValues.add(n)
            # return false if no duplicates in the set
        return False
        
        
        # Use hashset to place visited values
        # if value is in hashmap, then return true
        # else return false
        
        
        
        
        
        # passing nums[int]
        # return true is any value appears at least twice
        # return false if every element is distinct