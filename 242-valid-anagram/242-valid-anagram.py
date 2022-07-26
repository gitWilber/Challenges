class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use hashmaps to count the amount of times each character shows up in each string
        sCharCount = {}
        tCharCount = {}
        
        # if length of both strings aren't the same, they can't be anagrams
        if len(s) != len(t):
            return False
        # count chars in each string and put it in their hashmap
        else:
            for i in range(len(s)):
                # use .get() incase there is no key. without it, it will be an error
                sCharCount[s[i]] = 1 + sCharCount.get(s[i], 0)
                tCharCount[t[i]] = 1 + tCharCount.get(t[i], 0)
            
        # compare both hashmaps to see if the same
        if sCharCount != tCharCount:
            return False
        # return true if it passes both tests
        return True
            