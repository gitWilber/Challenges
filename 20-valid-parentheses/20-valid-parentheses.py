class Solution:
    def isValid(self, s: str) -> bool:
        # hashMap to show matching parentheses
        matchBrackets = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        
        # string is an array we can loop
        for char in s:
            # if closing bracket in hashmap
            if char in matchBrackets:
                # if stack is not empty and its last element is the matching bracket to char
                if stack and stack[-1] == matchBrackets[char]:
                    # pop stack
                    stack.pop()
                # else false because we can't add a closing bracket in the start
                else:
                    return False
            else:
                stack.append(char)
                
        # return true if stack is not empty, else return false
        return True if not stack else False
                