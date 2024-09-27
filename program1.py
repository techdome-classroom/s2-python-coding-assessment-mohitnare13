class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        
        for char in s:
            if char in bracket_map:  
                
                top_element = stack.pop() if stack else '#'
                
               
                if bracket_map[char] != top_element:
                    return False
            else:
                
                stack.append(char)

        # If the stack is empty, all brackets were properly matched
        return not stack

# Example usage
validator = Solution()
print(validator.isValid("()"))       
print(validator.isValid("()[]{}"))   
print(validator.isValid("(]"))  