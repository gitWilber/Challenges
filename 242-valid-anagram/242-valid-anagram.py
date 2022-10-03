class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        # if both string aren't same length, can't be anagrams
        if len(s) != len(t):
            return False
        
        # use 2 hashmaps to put the number of times each letter appears in each string
        hashmapS = {}
        hashmapT = {}
        
        # loop to fill up both hashmaps
        for i in range(len(s)):
            #  hashmap key will equal to count of current occurence
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
        
        # if both hashmaps are not the same
        if hashmapT != hashmapS:
            return False
        
        # if both strings are same length
        # if both occurence hashmaps are the same
        # then its an anagram
        return True
