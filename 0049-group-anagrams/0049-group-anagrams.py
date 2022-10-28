class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # use dictionary to store sortedWord : List of anagrams
        anagrams = {}
        
        # loop through array to check with dictionary
        for word in strs:
            # Sort word
            sortedWord = "".join(sorted(word))
            # if sorted word is not in the dictionary
            if sortedWord not in anagrams:
                anagrams[sortedWord] =[word]
            else:
                anagrams[sortedWord].append(word)
                
        # loop through dictionary values to put into result and return them
        result = []
        for item in anagrams.values():
            result.append(item)
        return result