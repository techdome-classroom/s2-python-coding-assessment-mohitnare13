class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
       
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            
            if char in mapping:
               
                top_element = stack.pop() if stack else '#'
                
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)

        # If stack is empty, all opening brackets are matched
        return not stack
