class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
       
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop the topmost element if stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the mapping is correct
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)

        # If stack is empty, all opening brackets are matched
        return not stack
