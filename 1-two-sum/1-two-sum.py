class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store numbers visited
        # difference variable
        numHash = {}
        diff = 0
        # loop thorugh nums array
        for i in range(len(nums)):
            # difference to see if it is in hashmap
            diff = target - nums[i]
            # if not in hashmap, store array num into hashmap
            if diff not in numHash:
                numHash[nums[i]] = i
            # else return both indices
            else:
                return numHash[diff], i
    