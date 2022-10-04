class Solution:
    def isValid(self, s: str) -> bool:
    
        
        # hashmap for matching brackets
        validBrackets = {')' : '(', '}' : '{', ']' : '['}
        # stack for pushing and popping elements
        stack = []
        
        # iterate through element in string
        for i in s:
            # if element is a closing bracket
            if i in validBrackets:
                # if stack is not empty and top element matches i in hashmap
                if stack and stack[-1] == validBrackets[i]:
                    # pop element in stack
                    stack.pop()
                # else stack is empty and first element is closing
                else:
                    return False
            # push into stack if opening bracket
            else:
                stack.append(i)
        # if the stack is empty
        if not stack:
            return True
                    
            